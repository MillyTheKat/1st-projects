# Making definitions for shorten the actual code.
def word_with_space(sentence):
    with_space = len(sentence.split()) + sentence.count(" ")
    return with_space

def no_space(space_sentence):
    return len(space_sentence.split())
# Starting actual code.
user_sentence = input(str("Please enter your sentence: "))
# Using loop to give answers and checking if the input is valid.
while True:
    user_choice = input("Please enter 1 for counting with space and 2 for counting without space (type 'quit' to stop): ")
    if user_choice == '1':
        print(f"Your sentence has {word_with_space(user_sentence)} words")
    elif user_choice == '2':
        print(f"Your sentence has {no_space(user_sentence)} words")
    elif user_choice == 'quit':
        print("Thank you and have a good day!")
        break
    else:
        print("Your choice is invalid. Please enter again!")
