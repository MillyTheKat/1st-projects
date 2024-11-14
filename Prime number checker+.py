pnc = int(input("Please enter: "))
divisors = [a for a in range(2, pnc) if pnc % a == 0]
factors = []
for num in divisors:
    while pnc % num == 0:
        factors.append(num)
        pnc //= num
if divisors:
    print("It's not a prime number!")
    print("Divisors:", divisors)
    print("Prime factors:", factors)
else:
    print("It's a prime number!")
