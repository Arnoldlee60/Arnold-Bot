### Arnold Bot for Discord

Arnold Bot is a versatile Discord bot designed to enhance user experience on servers with a variety of functionalities. It integrates seamlessly with the ChatGPT API to provide instant responses to questions, troubleshoot common issues, and offer problem-solving tools directly within your Discord community.

### Features

- **ChatGPT API Integration:** Leverage the power of ChatGPT to get instant answers to queries.
- **Custom Commands:** Easily create and manage custom commands for common tasks.
- **Problem Solving Tools:** Access a suite of tools designed to address frequent issues encountered by Discord users.
- **Reddit Links Embedd Properly:** The bot will take your reddit link and give you a proper link that will embedd a video or image properly with the link.

### Getting Started

To get started with Arnold Bot, you'll need to have Python installed on your machine. Follow the steps below to install the necessary dependencies and set up the bot on your server.

### Prerequisites

You need to create your own folder called txt_files:
Containing:
 1. BOT_NAME.txt //This is your bot discord name which needs to be in the format of "<@123456789>"
 2. chat_gpt_api.txt //ChatGPT Key you get from RapidAPI
 3. log.txt //This will be your log to be able to debug
 4. TOKEN.txt //The token you need to run your bot. You get this from creating your own bot from the discord website.

Ensure you have Python 3.6 or newer installed. You can check your Python version by running:
python --version
Installation
Install Required Packages:

Arnold Bot requires requests for handling API requests and discord for interacting with the Discord API. Install these packages using pip:

pip install requests 
pip install discord

Clone the Repository:
Clone the Arnold Bot repository from GitHub to your local machine:

git clone https://github.com/Arnoldlee60/Arnold-Bot.git
Configure the Bot:

Navigate to the Discord Developer Portal and create a new application to get your bot token. Replace the placeholder in the bot's configuration file with your actual bot token.

Run the Bot:
Navigate to the root directory of the cloned repository and run the main file to start the bot:


python main.py

This markdown file provides a structured and concise description of the Arnold Bot, including its features, installation instructions, contribution guidelines, licensing information, and support options. Adjust the GitHub URLs and specific instructions as necessary to match your actual repository and bot setup details.

About
The bot can be direct messaged and in a server it needs messaging permissions. 
In a discord server it must be tagged directly in order to work.

### Links
 1. https://discord.com/developers/applications 
 2. https://rapidapi.com/haxednet/api/chatgpt-api8/
