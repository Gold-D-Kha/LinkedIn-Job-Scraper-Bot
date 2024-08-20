# LinkedIn-Job-Scraper-Bot
LinkedIn Job Scraper Bot
This project is a LinkedIn job scraper bot that extracts job posts containing specific keywords and sends the details to a Telegram bot. The bot is built using Python and Selenium, and it automates the extraction of job posts from LinkedIn.

Prerequisites
# Before running the script, ensure you have the following installed:

Python 3.x
Selenium
Microsoft Edge WebDriver (or any other WebDriver if using a different browser)
A LinkedIn account
A Telegram bot token and chat ID
Installation
Clone the repository to your local machine:


git clone https://github.com/your-username/linkedin-job-scraper.git
Navigate to the project directory:


cd linkedin-job-scraper
Create a virtual environment (optional but recommended):


python -m venv venv
Activate the virtual environment:

# On Windows:

.\venv\Scripts\activate

# On macOS/Linux:

source venv/bin/activate
Install the required Python packages:


pip install -r requirements.txt
Configuration
Update the bot.py script with your LinkedIn credentials and Telegram bot details:

python
username_input.send_keys("your-email")  # Replace with your LinkedIn email
password_input.send_keys("your-password")  # Replace with your LinkedIn password

TOKEN = "your-telegram-bot-token"
CHAT_ID = "your-chat-id"
Update the path to your WebDriver:

python

service = Service("path-to-your-webdriver")
Running the Script
Ensure your WebDriver is executable and accessible.

Run the script:


python bot.py
The script will log in to LinkedIn, scroll through job posts, and send relevant posts to your Telegram bot.

Notes
The script is set to skip posts containing the keyword "India."
The script will continue to run until manually stopped. Press Enter to stop the script and close the browser.
Troubleshooting
Timeout Errors: Ensure that your internet connection is stable. If the connection times out frequently, consider increasing the wait time in the script.
CAPTCHA: If LinkedIn prompts for CAPTCHA verification, manually complete the verification.
