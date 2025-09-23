import requests
import random

print("Welcome to Word Chain Game. If you want to stop the game, type 'I quit'. Please start your word")

while True:
    player = input("Your turn: ").lower()
    if player == "i quit":
        print("Thank you for playing.")
        break
    word_check = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{player}")
    if word_check.status_code == 200:
        found_in_dictionary = word_check.json()
        if len(found_in_dictionary) > 0:
            last_letter = player[-1]

            computer_word = requests.get(f"https://api.datamuse.com/words?sp={last_letter}*&max=100")
            if computer_word.status_code == 200:
                word_list = [word['word'] for word in computer_word.json()]
                if word_list:
                    computer = random.choice(word_list)
                    print(f"My word is {computer}. Your turn.")
                else:
                    print("I lose! Congratulation!")
                    break
            else:
                print(" ")
    else:
        print("Word does not exist. Please try again")
