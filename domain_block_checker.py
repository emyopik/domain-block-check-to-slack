import requests
import logging
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone, timedelta

# Setup for Slack Webhook URL and the file containing domain links
WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "#")
FILE_LINKS = "#"

# Setup logging configuration to log both to a file and to the console
logging.basicConfig(filename='link_checker.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
root = logging.getLogger()
handler = logging.StreamHandler()
root.addHandler(handler)

# Define the timezone for GMT+7 (WIB)
WIB = timezone(timedelta(hours=7))

def get_current_time():
    """Get the current time formatted for logging and notifications in WIB timezone"""
    return datetime.now(WIB).strftime('[%A / %d %B %Y %H:%M:%S]')

def load_links_from_file(filename):
    """Load a list of domain links from the specified file"""
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def normalize_url(url):
    """Normalize a URL by removing the protocol (http/https) and trailing slash if present"""
    # Remove 'http://' or 'https://' if present
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
    # Remove trailing slash if present
    if url.endswith("/"):
        url = url[:-1]
    return url

def check_domain(domain):
    """Check if the domain is blocked using the checkdomain API"""
    domain = normalize_url(domain)  # Normalize the URL to ensure proper API response
    try:
        # Perform a GET request to the checkdomain API
        response = requests.get(f"https://check.skiddle.id/?domain={domain}&json=true")
        response.raise_for_status()  # Raise an exception for any failed request
        result = response.json()
        # Return the 'blocked' status of the domain; default to True (blocked) if no data is available
        return result.get(domain, {}).get('blocked', True)
    except requests.RequestException as e:
        # Log the error if the request fails and assume the domain is blocked
        logging.error(f"Failed to check domain {domain}. Error: {e}")
        return True  # Default to blocked on error

def send_notification_to_slack(message):
    """Send a notification message to Slack using the specified webhook URL"""
    payload = {"text": message}
    try:
        # Send the notification via POST request to Slack webhook
        response = requests.post(WEBHOOK_URL, json=payload)
        response.raise_for_status()  # Raise an exception if the request fails
    except requests.RequestException as e:
        # Log the error if the notification fails
        logging.error(f"Failed to send notification to Slack. Error: {e}")

def handle_link(link):
    """Process and check the status of a single domain link"""
    logging.info(f"Starting to check domain: {link}")
    try:
        # Check if the domain is blocked
        is_blocked = check_domain(link)
        if is_blocked:
            # Log and notify if the domain is blocked
            message = f"[{get_current_time()}] Domain {link} is BLOCKED - NEEDS REPLACEMENT"
            logging.info(message)
            send_notification_to_slack(message)
            return link, True
        else:
            # Log and notify if the domain is safe
            message = f"[{get_current_time()}] Domain {link} is safe."
            logging.info(message)
            send_notification_to_slack(message)
            return link, False
    except Exception as e:
        # Log any unexpected errors that occur during the domain check
        logging.error(f"Failed to check domain {link}. Error: {e}")
        return link, True  # Default to blocked in case of error

if __name__ == "__main__":
    logging.info("Starting domain checking process")

    try:
        # Load the list of domain links from the specified file
        domain_list = load_links_from_file(FILE_LINKS)
    except Exception as e:
        # Log the error and exit if the file cannot be read
        logging.error(f"Failed to read file {FILE_LINKS}. Error: {e}")
        sys.exit(1)

    MAX_THREADS = 5  # Define the maximum number of concurrent threads

    # Use ThreadPoolExecutor to process multiple domain checks concurrently
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(handle_link, link) for link in domain_list]

        blocked_links = []
        for future in futures:
            try:
                # Gather results from each thread
                link, is_blocked = future.result()
                if is_blocked:
                    blocked_links.append(link)
            except Exception as e:
                # Log any errors that occur during thread execution
                logging.error(f"Error occurred in one of the threads: {e}")

        total_links = len(domain_list)
        total_blocked = len(blocked_links)

        # Send a summary notification to Slack with the results
        summary_message = f"Checked {total_links} domains successfully at {get_current_time()}. Blocked domains: {', '.join(blocked_links)}"
        send_notification_to_slack(summary_message)

    logging.info("Completed domain checking process")
