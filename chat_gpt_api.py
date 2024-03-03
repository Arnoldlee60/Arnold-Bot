import requests
import json
from datetime import datetime
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

Key = ""
with open('txt_files/chat_gpt_api.txt', 'r') as file:
    Key = file.readline().strip()

def chat_gpt(message) -> str:
    url = "https://chatgpt-api8.p.rapidapi.com/"

    payload = [
        {
            "content": message,  # Use the message variable directly
            "role": "user"
        }
    ]
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()  # Directly convert response to JSON

    with open("txt_files/log.txt", "a") as file:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"{current_time}, CHATGPT SERVER RESPONSE CODE: {response.status_code}\n")
        file.write(f"{current_time}, CHATGPT JSON: {data}\n")
        file.write(f"{current_time}, CHATGPT response: {data.get('text')}\n")
    
    return data.get("text", "ERROR")  # Safely get 'text' or return an error message