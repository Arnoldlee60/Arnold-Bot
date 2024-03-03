import discord
import responses
import chat_gpt_api
from datetime import datetime

intents = discord.Intents.default()  # This enables the default intents
intents.messages = True  # If you want to receive messages
client = discord.Client(intents=intents)
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
TOKEN = ""
BOT_NAME = ""

with open('txt_files/TOKEN.txt', 'r') as file:
    TOKEN = file.readline().strip()

with open('txt_files/BOT_NAME.txt', 'r') as file:
    BOT_NAME = file.readline().strip()

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

        with open("txt_files/log.txt", "a") as file:
            file.write(f"{current_time}, {client.user} responded with: {response}\n")

    except Exception as e:
        print(e)
        with open("txt_files/log.txt", "a") as file:
            file.write(f"ERROR: {e} @{current_time}\n")

async def reddit_embed(message, user_message, is_private):
    try:
        response = responses.replace_reddit_url(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

        with open("txt_files/log.txt", "a") as file:
            file.write(f"{current_time}, {client.user} responded with: {response}\n")

    except Exception as e:
        print(e)
        with open("txt_files/log.txt", "a") as file:
            file.write(f"ERROR: {e} @{current_time}\n")

async def banned_message(message, user_message, is_private):
    try:
        response = responses.banned_people()
        await message.author.send(response) if is_private else await message.channel.send(response)

        with open("txt_files/log.txt", "a") as file:
            file.write(f"{current_time}, {client.user} responded with: {response}\n")

    except Exception as e:
        print(e)
        with open("txt_files/log.txt", "a") as file:
            file.write(f"ERROR: {e} @{current_time}\n")

async def chat_gpt_question(message, user_message, is_private):
    try:
        response = chat_gpt_api.chat_gpt(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

        with open("txt_files/log.txt", "a") as file:
            file.write(f"{current_time}, {client.user} responded with: {response}\n")

    except Exception as e:
        print("Exception: " + e)
        with open("txt_files/log.txt", "a") as file:
            file.write(f"ERROR: {e} @{current_time}\n")

def run_discord_bot():
    @client.event
    async def on_ready():
        print(f'{client.user} is now running on: ' + current_time)
        with open("txt_files/log.txt", "a") as file:
            file.write(f"{current_time}, {client.user} is now running\n")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        guild = str(message.guild)
        channel = str(message.channel)

        #log this later
        #print(f"{username} said: '{user_message}' on Server: {guild} on Channel: {channel}")
        with open("txt_files/log.txt", "a") as file:
            if user_message:
                if str(message.author) in responses.ban_list():
                    file.write(f"Time: {current_time}, Banned User {username} said: '{user_message}', Server: {guild}, Channel: {channel} \n")
                else:
                    file.write(f"Time: {current_time}, {username} said: '{user_message}', Server: {guild}, Channel: {channel} \n")

        if user_message.startswith(BOT_NAME):
            parts = user_message.split(' ')
            user_message = ' '.join(parts[1:])

        if user_message:
            is_private = False
            if channel.startswith("Direct Message with"):
                is_private = True

            if str(message.author) in responses.ban_list():
                await banned_message(message, user_message, is_private)
            else:
                if user_message.startswith("https://www.reddit.com"):
                    temp = message
                    if is_private == False:
                        await message.delete()

                    await reddit_embed(temp, user_message, is_private)
                else:
                    await chat_gpt_question(message, user_message, is_private)
                # elif user_message[-1] == "?":
                #     await chat_gpt_question(message, user_message, is_private)
                #     #await gemini_question(message, user_message, is_private)
                # else:
                #     await send_message(message, user_message, is_private)

    client.run(TOKEN)