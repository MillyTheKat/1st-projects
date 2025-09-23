import random
game = ["Rock", "Scissors", "Paper"]
player = input("Please enter Rock, Scissors, Paper: ").capitalize()
computer = random.choice(game)
# print("Computer chose", computer)
# diff = (game.index(player) - game.index(computer)) % len(game)
#
# if diff == 0:
#     print("It's a tie!")
# elif diff == 1:
#     print("You lose!")
# else:
#     print("You win!")

if player == computer:
    print("It's a tie!")
elif (player == "Rock" and computer == "Scissors") or \
      (player == "Scissors" and computer == "Paper") or \
      (player == "Paper" and computer == "Rock"):
    print("You win!")
else:
    print("You lose!")
