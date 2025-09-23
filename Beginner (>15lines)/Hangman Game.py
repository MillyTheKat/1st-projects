import requests
import random


def random_word(mode):
    if mode == "survivor":
        url = "https://api.datamuse.com/words?sp=?????"
    elif mode == "veteran":
        url = "https://api.datamuse.com/words?sp=????????"
    elif mode == "hardcore":
        url = "https://api.datamuse.com/words?sp=??????????????"
    else:
        return None

    computer = requests.get(url)
    if computer.status_code == 200:
        words = computer.json()
        if words:
            return random.choice(words)['word']
        else:
            return None
    else:
        print("Error")
        return None


def display_update_word(player_choice, display_words, guessing):
    for index, letter in enumerate(player_choice):
        if letter == guessing:
            display_words[index] = guessing
    return display_words


print("Welcome to the Hangman Game. I give you 10 hearts. Please don't die!")

while True:
    level = input("Please choose the level (Survivor, Veteran, Hardcore): ").lower()
    quiz = random_word(level)
    if quiz:
        break
    print("Please enter again")

display_word = ["*"]*len(quiz)
hearts = 10
print("My word is "+"".join(display_word))

while hearts > 0 and "*" in display_word:
    guess = input("Please enter your guess: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid. Please enter a single letter!")
        continue

    if guess in quiz:
        display_word = display_update_word(quiz, display_word, guess)
        print("Good guess! Word now: "+"".join(display_word))
    else:
        hearts -= 1
        print(f"Wrong guess. you lost a heart. your {hearts} hearts remaining.")

if "*" not in display_word:
    print("Congratulations. You win the game! The word is " + quiz)
else:
    print("Sorry, you lost. Try your best next time.")
