numbers = list(range(1, 101))
for a in numbers:
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        print(a)
