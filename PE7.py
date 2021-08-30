"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

print("Please enter a number to check for prime or not: ")
userInput = int(input())


for x in range(1, userInput):
    for y in range(1,userInput):
        print("This loop is in y " + str(y) + " times!")
    print("This loop is in x " + str(x) + " times!")
#while counter <= userInput:
    #if((userInput % counter == 0) & (userInput % 1 == 0)):
    #    primeCounter.append(userInput)
    #counter += 1