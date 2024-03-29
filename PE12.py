"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

    Answer = 76576500 : 576

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
"""
inPutNumber = 25000
triangularArray = []
factorsArray = []
numberSum = 0

for x in range(1, inPutNumber):
    numberSum += x
    triangularArray.append(numberSum)
    #print(f"{x} : {numberSum}")


for k in triangularArray:
    factorsCounter = 0    
    for l in range(1, k + 1):
        if(((k % l) == 0)):
            factorsArray.append(l)
            factorsCounter = factorsCounter + 1
    print(f"{k} : {factorsCounter}")
"""


n = 1
triangularArray = []
factorsArray = []
numberSum = 0

while (n > 0):
    numberSum += n
    #triangularArray.append(numberSum)
    factorsCounter = 0
    if(numberSum % 2 == 1):
        n = n + 1
        continue
    else:
        for l in range(1, numberSum + 1):
            if(((numberSum % l) == 0)):
                factorsCounter += 1
            #factorsArray.append(factorsCounter)
        if(factorsCounter >= 500):
            print(f"{numberSum} : {factorsCounter}")
            break
        else:
            print(f"{numberSum} : {factorsCounter}")
        n = n + 1


"""
2023066 : 8
2025078 : 32
2031120 : 240
"""

"""
n = 1
triangularArray = []
factorsArray = []
numberSum = 0

while (n > 0):
    numberSum += n
    #triangularArray.append(numberSum)
    factorsCounter = 0
    for l in range(1, numberSum + 1):
        if(((numberSum % l) == 0)):
            factorsCounter += 1
        #factorsArray.append(factorsCounter)
    if(factorsCounter > 200):
        print(f"{numberSum} : {factorsCounter}")
        break
    else:
        print(f"{numberSum} : {factorsCounter}")
    n = n + 1
"""

"""
2027091 : 32
2029105 : 32
2031120 : 240"""