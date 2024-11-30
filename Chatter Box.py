import random
from datetime import datetime


def generate_random_color():
    color_code = random.randint(0, 255)
    return f"\033[38;5;{color_code}m"


colors = generate_random_color()
users = {}

while True:
    chatter = input("Welcome to Chatter Box. Please enter your name (No longer than 5 letters) to begin.\nMy name is: ")
    if len(chatter) < 5 and chatter not in users:
        users[chatter] = generate_random_color()
        print(f"Welcome{chatter}! Enjoy your time!")
    else:
        print("The name is too long or already taken. Please try the new one.")
