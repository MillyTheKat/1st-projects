import random

players = {}
race_distance = 30

while len(players) < 4:
    name = input("Please enter your name: ").strip()
    if name in players:
        print("This name is already taken. Please choose the other name.")
    else:
        boat_name = input("Enter your boat's name: ").strip()
        players[name] = {'boat': boat_name, 'position': 0}
        print(f"Welcome {name}. Your {boat_name} is ready.")

print("The race will be start shortly.")

finish_line = False
while not finish_line:
    for name, info in players.items():
        players[name]['position'] += random.randint(1, 3)
        boat_name = info['boat']
        position = info['position']
        race = "=" * position + boat_name

        print(f"{name}: {race}")

        if position >= race_distance:
            print(f"Congratulation, {name}! You will have a very lucky year.")
            finish_line = True
