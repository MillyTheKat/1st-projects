def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)

a = int(input("Please in put your number:"))
if a > 0:
    print(factorial(a))
else:
    print("Invalid. PLease try again")
