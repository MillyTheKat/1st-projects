pn = int(input("Please enter the number:"))
divisors = [a for a in range(2, pn) if pn % a == 0]
if pn > 1 and any(pn % a == 0 for a in range(2, pn)):
    print("It's not a prime number")
    print("Divisor(s):", divisors)
else:
    print("It's a prime number")
