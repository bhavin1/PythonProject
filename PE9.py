"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math
import random


sum = 0
counter = 0
while sum != 1000:
    counter += 1
    a = random.randint(195, 205)
    b = random.randint(370, 380)
    
    powA = pow(a, 2)
    powB = pow(b, 2)


    powSum = powA + powB
    c = math.sqrt(powSum)
    sum = a + b + c
    print(str(counter) + " = a " + str(a) + " : " + " b " + str(b) + " :" + " c " + str(c) + " = " + str(sum))
    
    