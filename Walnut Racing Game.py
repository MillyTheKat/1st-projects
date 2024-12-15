import random
import time


def generate_random_color():
    color_code = random.randint(0, 255)
    return f"\033[38;5;{color_code}m"


players = {}
race_distance = 30
n = int(input("Please enter the number of player: "))

while len(players) < n:
    name = input("Please enter your name: ").strip()
    if name in players:
        print("This name is already taken. Please choose the other name.")
    else:
        boat_name = input("Enter your boat's name: ").strip()
        players[name] = {'boat': boat_name, 'position': 0, 'color': random.randint(0, 255)}
        print(f"Welcome {name}. Your {boat_name} is ready.")

print("The race will be start shortly.")
max_indent = max(map(len, players.keys()))

finish_line = False
while not finish_line:
    for name, info in players.items():
        players[name]['position'] += random.randint(1, 3)
        boat_name = info['boat']
        position = info['position']
        color = info['color']
        race = "=" * position + boat_name
        indent = " " * (max_indent - len(name))

        print(f"\033[38;5;{color}m{name}: {indent}{race}\033[0m")

        if position >= race_distance:
            print(f"Congratulations, \033[38;5;{color}m{name}\033[0m! You will have a very lucky year.")
            finish_line = True
    if not finish_line:
        time.sleep(1)
        print(f"\033[{n + 1}A\033[2K")
