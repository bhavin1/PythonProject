from typing import Concatenate, Literal
import math
from decimal import Decimal

"""name = "Bhavin"
age = 30

print(f"My name is {name} and i'm {age} old. The lengh of my name is {len(name)}.")

print("{} is {} years old.".format(name, age))


for x in range(1, 5):
    if (x > 1):
        print("Iterating loop {} times.".format(x))
    else:
        print("Iterating loop {} time.".format(x))

for y in range(4):
    print(f"Loop has run {y} times.")


if age > 20 and name == "Bhavin":
    print("It is Bhavin")
else:
    print("It's not Bhavin!")


animals = ["Dog", "Cat", "Lion", "Elephant", "Tiger", "Horse"]
print(animals)
animals.insert(1,"Zebra")
print(animals)"""

for x in range(2, 1000):
    v = Decimal(1/x)
    print(f"{v.as_tuple().exponent} = {v}")
    #print(v.as_tuple().exponent)


