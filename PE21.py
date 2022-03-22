""" Problem 21  Solved!
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


from itertools import count


amicableArray = []
amicableArrayTwo = []
resultArray = []
finalAnswer = 0

searchAmicleNumber = 10000

def findAmicable(inputNumber):
    tempSum = 0
    #swapInput = 0
    counter = 1
    for x in range(1, inputNumber):
        if((inputNumber % x) == 0):
            tempSum = tempSum + x
            #print(x)
    amicableArray.append(tempSum)
    #print(f"{inputNumber} : {tempSum}")



for x in range(1, searchAmicleNumber):
    findAmicable(x)

for y in amicableArray:
    tempSum = 0
    for z in range(1, y):
        if((y % z) == 0):
            tempSum = tempSum + z
            #print(x)
    amicableArrayTwo.append(tempSum)
    #print(f"{y} : {tempSum}")



for t in range(0, searchAmicleNumber):
    if(t == amicableArrayTwo[t - 1]) and (t != amicableArray[t - 1]):
        resultArray.append(amicableArray[t - 1])
    #print(f"{t} === {amicableArray[t - 1]} === {amicableArrayTwo[t - 1]}")


for f in resultArray:
    finalAnswer += f

print(finalAnswer)
