

primeSum = 0
for x in range(80):
    p = (((pow(x, 2))-(79*x)+1601))
    primeSum += p
    print(f"{x} = {p}")
print(primeSum)