"""
Euler discovered the remarkable quadratic formula:

It turns out that the formula will produce 40 primes for the consecutive integer values . However, when is divisible by 41, and certainly when

is clearly divisible by 41.

The incredible formula
was discovered, which produces 80 primes for the consecutive values

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

, where and

where
is the modulus/absolute value of
e.g. and

Find the product of the coefficients,
and , for the quadratic expression that produces the maximum number of primes for consecutive values of , starting with .
"""

primeSum = 0
for x in range(80):
    p = (((pow(x, 2))-(79*x)+1601))
    primeSum += p
    print(f"{x} = {p}")
print(primeSum)