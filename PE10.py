""" The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million. """

counter = 1
startingNumber = 1
terms = 1
termsArray = [0]

for x in range(startingNumber, 1000000):
    while x != 1:
        if((x % 2) == 0):
            x = x / 2
            terms += 1
        else:
            x = ((3*x) + 1)
            terms += 1
    termsArray.append(terms)
    print(str(counter) + ": " + str(terms))
    terms = 1
    counter += 1

x = termsArray.index(525)
termsArray.sort(reverse=False)
print(termsArray)
print(x)

"""while counter <= 100:
    while startingNumber != 1:
        if((startingNumber % 2) == 0):
            startingNumber = startingNumber / 2
            terms += 1
        else:
            startingNumber = ((3*startingNumber) + 1)
            terms += 1
    print(str(counter) + ": " + str(terms))
counter += 1"""
    