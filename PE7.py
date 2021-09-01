"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

print("Please enter a number to check for prime or not: ")
userInput = int(input())
PrimeList = []
counter = 1
primeSum = 0

for num in range(1, userInput + 1):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            PrimeList.append(num)

for x in PrimeList:
    primeSum = primeSum + x
    #print(x)
print(len(PrimeList))
print(primeSum)