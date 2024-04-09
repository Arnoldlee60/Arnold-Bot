import random

Greetings = ['hello', 'hi', 'hey', 'greetings', 'salutations', 'howdy', 'welcome', 'bonjour', 'hola', 'ciao', 'hallo', 'salaam', 'namaste', 'ahoy', 'aloha', 'shalom', 'hiya', 'yo', 'sup', 'whazzup']

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message in Greetings:
        return 'Hey there!'
    elif p_message == '!help':
        return 'No'
    else:
        return "I don't have a command for that"

def replace_reddit_url(url: str) -> str:
    res = 'https://www.rxddit.com' + url[len('https://www.reddit.com'):]
    return res + " Here is your embedded link!"
    
def banned_people() -> str:
    return "Nold told me not to talk to you"

def ban_list() -> list:
    return ["Example_Person"]

def commands(message: str) -> list:
    if message.startswith("https://www.reddit.com"):
        return replace_reddit_url(message)
