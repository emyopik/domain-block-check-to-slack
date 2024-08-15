# Domain Block Checker with Slack Notifications

**Domain Block Checker with Slack Notifications** is a Python script designed to check whether a domain is blocked using an external API. The script loads a list of domains from a text file, checks their status, and sends notifications to Slack if any of the domains are blocked.

## Features

- **Parallel Processing**: Check multiple domains concurrently using `ThreadPoolExecutor`.
- **Slack Notifications**: Send notifications to Slack if a domain is blocked.
- **Logging**: All activities are logged into a file for debugging and auditing purposes.

## Requirements

- Python 3.x
- Python packages:
  - `requests`
  - `logging`

You can install the dependencies using pip:

```bash
pip install requests
```

## Usage

1. **Environment Setup**:
   - Set your Slack webhook URL in the `SLACK_WEBHOOK_URL` environment variable.
   - Specify the path to the text file containing the list of domains to be checked in the `FILE_LINKS` variable.

2. **Domain File**:
   - Create a text file containing a list of domains (one domain per line) that you want to check.

3. **Run the Script**:
   - Run the script with the following command:
   
   ```bash
   python domain_block_checker.py
   ```

4. **Results**:
   - The script will check the status of each domain and send a notification to Slack if any domains are blocked. All results are also logged in the `link_checker.log` file.

## Project Structure

```
.
├── domain_block_checker.py  # Main script to check domain status
├── link_checker.log         # Log file to record checking results
└── README.md                # Project documentation
```

## Code Explanation

- **get_current_time()**: Returns the current time formatted for logging and notifications.
- **load_links_from_file(filename)**: Loads the list of domains from a text file.
- **normalize_url(url)**: Removes protocol and trailing slash from the URL to ensure proper API response.
- **cek_domain(domain)**: Checks the block status of the domain using an external API.
- **kirim_notifikasi_ke_slack(pesan)**: Sends a notification to Slack.
- **handle_link(link)**: Manages the checking process for a single domain and sends a notification if the domain is blocked.

## Acknowledgments

Special thanks to [Skiddle-ID](https://github.com/Skiddle-ID/checkdomain) for providing the API used in this project to check domain statuses.

## Contributions

Contributions are always welcome! If you have suggestions or find any bugs, feel free to open an issue or submit a pull request.
