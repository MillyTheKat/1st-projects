import requests

word = input("Please enter the first word: ")
response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
if response.status_code == 200:
    found_in_dictionary = response.json()
    if found_in_dictionary.size() > 0:
        print("Word exists")
    else:
        print("Word does not exist")
else:
    print("Error searching in dictionary")
