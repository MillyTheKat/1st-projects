import random
random_number = random.randint(1,100)
print("Please guess the number from 1 to 100")
while True:
    guess = int(input("My guess is:"))
    if guess == random_number:
        print("Congratulation. You're correct!")
        break
    else:
        print("Incorrect. Please try again.")
        if guess < random_number:
            print("It's higher number")
        else:
            print("It's lower number")
