""" Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

#a = 20
divStoreArray = []
divSumArray = []
d2 = []

def amicable(currentNumber):
    tempSum_1 = 0
    for i in range(1, currentNumber):
        if(((currentNumber % i) == 0)):
            divStoreArray.append(i)
            tempSum_1 += i
    divSumArray.append(tempSum_1)
    print(str(currentNumber) + ": " + str(divSumArray))
    #print(str(currentNumber) + ": " + str(divStoreArray) + str(divSumArray))
    #print(divSumArray)

def otherAmicable(num):
    tempSum_2 = 0
    for i in range(1, num):
        if(((num % i) == 0)):
            tempSum_2 += i
    d2.append(tempSum_2)
    print(str(i) + ": " + str(d2))

print("===========Run 1===========")
for x in range(1, 11):
    divStoreArray.clear()
    divSumArray.clear()
    amicable(x)

for x in divSumArray:
    d2.clear()
    otherAmicable(x)

























"""b = 20
divisorArray = []
divSumArray = []

def amicable(n):
    factorSum = 0
    for x in range(1,n):
        if((n % x) == 0):
            divisorArray.append(x)
            divSumArray.append(x)
    calculateSum(divSumArray)
    print(str(n) + ":" + str(divisorArray) + ": " + str(factorSum))
    factorSum = 0
    divisorArray.clear()

    amicableNumSum = 0
    for x in divisorArray:
        amicableNumSum += x
    print(str(divisorArray) + " = " + str(amicableNumSum))
    divisorArray.append(amicableNumSum)


def calculateSum(a):
    amicableNumSum = 0
    for x in a:
        amicableNumSum += x
    #divSumArray.append(amicableNumSum)
    print(divSumArray)
    divSumArray.clear()

for i in range(1, b + 1):
    amicable(i)
#print(divisorArray)
calculateSum(divisorArray)
#amicable(220)
#calculateSum(divisorArray)"""
