""" Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from typing import Match

palArray = []


for i in range(1,1000):
    for j in range(1,1000):
        prod = str(i * j)
        if((len(prod) % 2) == 0):
            palArray.append(prod)
        """for c in len(conToStr):
            if(conToStr.index(x) == )
        print(str(j) + " x " + str(i) + " = " + str(prod))"""

resultArray = []
def compare():
    match = 0
    currentNumber = 0
    for i in palArray:
        currentNumber = i
        for x, y in zip(currentNumber, reversed(currentNumber)):
            if(match == (len(currentNumber)/2)):
                #print(currentNumber)
                resultArray.append(currentNumber)
            if x == y:
                match += 1
            else:
                break
        match = 0
    print(resultArray)

compare()