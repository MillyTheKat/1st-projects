pnc = int(input("Please enter your number: "))
divisor = 2
factors = []
while divisor <= pnc:
    if pnc % divisor == 0:
        factors.append(divisor)
        pnc //= divisor
    else:
        divisor += 1

print("Prime factors:", factors)
print("Divisors:", set(factors))
print("Prime number:", len(factors) == 1)
