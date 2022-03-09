"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

p = 29
divisorArray = []
abundantDict = {}
deficientDict = {}

for p in range(1, p):
    divisorSum = 0
    for i in range(1, p):
        if(p % i == 0):
            divisorArray.append(i)
            divisorSum += i
        if (divisorSum >= p) :
            abundantDict.update({p:divisorSum})
        else:
            deficientDict.update({p:divisorSum})

#print(divisorArray)
for abuK, abuV in abundantDict.items():
    print(abuK, abuV)

for defK, defV in deficientDict.items():
    print(defK, defV)