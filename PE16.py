""" 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000? """

import math
from typing import Iterator

x = pow(2,1000)
conToStr = str(x)

strArray = []
iterator = 0

for i in range(len(conToStr)):
    slice = conToStr[i:i+1]
    strArray.append(slice)

testArray = []

numberSum = 0

for j in strArray:
    numberSum += int(j)

print(numberSum)
#print(conToStr.index('2'))
#print(conToStr)
#print(strArray)