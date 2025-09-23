import random
from datetime import datetime


def generate_random_color():
    color_code = random.randint(0, 255)
    return f"\033[38;5;{color_code}m"


users = {}


def display_message(user_name, user_color, message):
    timestamp = datetime.now().strftime("%H:%M")
    print(f"{user_color}{user_name}({timestamp}): {message}\033[0m")


print("Welcome to Chatter Box! Please enter 'exit' to leave the chat anytime.")

chatter = None
while chatter is None:
    name = input("Please enter your name (max 8 letters) to begin.\nMy name is: ").strip()
    if name == "":
        print("Please enter a valid name.")
    elif len(name) >= 8:
        print("The name is too long. Please try the new one.")
    elif name in users:
        print("The name is already taken. Please try a new one.")
    else:
        chatter = name

users[chatter] = generate_random_color()
print(f"Welcome {chatter}! Enjoy your time!")

while True:
    message = input(f"{chatter}: ").strip()
    if message.lower() == "exit":
        print(f"{users[chatter]}{chatter} has left the chat. Goodbye!\033[0m")
        del users[chatter]
        break

    display_message(chatter, users[chatter], message)