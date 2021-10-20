"""
Multiline comment in Python. In this section we'll do the exerice how to get user input.
"""
"""userInput = str(input())
print(userInput)"""

testString = 3003
conToString = str(testString)
revString = reversed(conToString)

if((len(conToString) % 2) == 0):
    print("It's an even digit number!")
print(len(conToString))

def compate(a,b):
    match = 0
    for x, y in zip(a, b):
        if x == y:
            match += 1
    print(match)

compate(conToString, revString)
"""revTestString = reversed(conToString)

for y in revTestString:
    print(y)"""