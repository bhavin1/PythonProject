"""Recursion in Python"""

def py_recursion(n):
    if(n < 0):
        print("Incrorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return py_recursion(n - 1) + py_recursion(n - 2)

userInput = int(input("Enter the number you want to find Fibbonacci Sequence for:"))

for x in range(userInput):
    print(py_recursion(x))

"""print(py_recursion(40))"""