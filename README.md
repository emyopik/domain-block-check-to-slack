# Domain Block Checker with Slack Notifications

**Domain Block Checker with Slack Notifications** is a simple Python script that checks if a list of website domains is blocked. It uses an external service to check the status of the domains and sends notifications to Slack if any of the domains are blocked.

## What This Script Does

- Loads a list of website domains from a text file.
- Checks each domain to see if it’s blocked using an online service.
- Sends a message to your Slack workspace if any of the domains are blocked.
- Keeps a log of all the activities in a file.

## Who Is This For?

This script is for anyone who needs to regularly check if a list of domains is blocked, but you don't need to be a coding expert to use it! If you know how to copy and paste, you can set this up.

## What You Need to Get Started

1. **Python 3**: This script runs on Python 3, a programming language that’s easy to learn. Don’t worry if you’ve never used it before. You can download Python 3 from [python.org](https://www.python.org/downloads/). Make sure you choose the latest version for your operating system.

2. **Slack Webhook URL**: This is a special link that allows the script to send messages to a Slack channel. You can create one by following these steps:
   - Go to your Slack workspace.
   - Create a new app at [Slack API: Your Apps](https://api.slack.com/apps).
   - Under "Add features and functionality," select "Incoming Webhooks."
   - Activate "Incoming Webhooks" and add a new webhook to your workspace.
   - Copy the webhook URL provided. You’ll need it later.

3. **Text Editor**: You can use Notepad on Windows, TextEdit on Mac, or any simple text editor to edit the script.

## How to Set Up the Script

1. **Install Python Packages**:
   - Open the command prompt (Windows) or terminal (Mac/Linux).
   - Type the following command and press Enter to install the necessary Python packages:
     ```bash
     pip3 install requests
     ```

2. **Download the Script**:
   - Copy the script from this page into a new file named [`domain_block_checker.py`](https://github.com/emyopik/domain-block-check-to-slack/blob/main/domain_block_checker.py) using your text editor.
   
3. **Prepare Your List of Domains**:
   - Create a simple text file using your text editor.
   - List all the domains you want to check, one per line, like this:
     ```
     example.com
     another-example.com
     third-example.org
     ```
   - Save this file as `domains.txt` (or another name, but remember it).

4. **Edit the Script**:
   - Open the `domain_block_checker.py` file in your text editor.
   - Find the line that says:
     ```python
     WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "#")
     ```
   - Replace `"#"` with your Slack webhook URL in quotes:
     ```python
     WEBHOOK_URL = "https://hooks.slack.com/services/your/webhook/url"
     ```
   - Find the line that says:
     ```python
     FILE_LINKS = "#"
     ```
   - Replace `"#"` with the name of your domains file in quotes:
     ```python
     FILE_LINKS = "domains.txt"
     ```

5. **Run the Script**:
   - Open the command prompt (Windows) or terminal (Mac/Linux).
   - Navigate to the folder where you saved the script and the domains file. For example:
     ```bash
     cd path_to_your_folder
     ```
   - Run the script by typing:
     ```bash
     python3 domain_block_checker.py
     ```

6. **Check the Results**:
   - The script will start checking the domains. If any are blocked, it will send a message to your Slack channel.
   - You can also check the `link_checker.log` file that will be created in the same folder to see all the activities.

## Troubleshooting

- **Python Not Recognized**: If you get a message that Python is not recognized, make sure you installed it correctly and that it’s added to your system’s PATH.
- **Errors in the Script**: If the script gives an error, double-check that the webhook URL and file name are correct and properly formatted in quotes.
- **Slack Notifications Not Working**: Make sure the webhook URL is correct and that your Slack workspace is active.

## Acknowledgments

Special thanks to [Skiddle-ID](https://github.com/Skiddle-ID/checkdomain) for providing the API used in this project to check domain statuses.
