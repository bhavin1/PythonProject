"""Calculate Fibbinaci Series"""

import math

print("Enter the number to find the Fib sequence for:")

def findFibinacci(n):
    if(n <= 1):
        return n
    else:
        return (findFibinacci(n -1) + findFibinacci(n -2))

nterms = int(input())

#Check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer!")
else:
    print("Fibonacci Sequence:")
    for i in range(nterms):
        print(findFibinacci(i))