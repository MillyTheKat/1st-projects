print("Password length must be at least 8 characters.")
print("Password must contain at least one digit (0-9).")
print("Password must contain at least one uppercase letter.")
print("Password must contain at least one lowercase letter.")
def number_checking():
    count = 0
    for n in user:
        if n.isdigit():
            count += 1
    return count

def upper_letter_checking():
    upper_letter = 0
    for i in user:
        if i.isupper():
            upper_letter += 1
    return upper_letter

def lower_letter_checking():
    lower_letter = 0
    for a in user:
        if a.islower():
            lower_letter += 1
    return lower_letter

while True:
    user = input("Create password: ")
    if len(user) <8:
        print("Password is too short!")
    elif number_checking() < 1:
        print("Password needs a digit!")
    elif upper_letter_checking() < 1:
        print("Password needs an upper letter!")
    elif lower_letter_checking() < 1:
        print("Password needs a lower letter!")
    else:
        print("Password is strong!")
        break