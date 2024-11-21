import random

import requests

player = input("Your turn: ").lower()
word_check = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{player}")
if word_check.status_code == 200:
    found_in_dictionary = word_check.json()
    if len(found_in_dictionary) > 0:
        last_letter = player[-1]


        computer = random.choice(list_word)
    else:
        print("Word does not exist")
else:
    print("Error searching in dictionary")
