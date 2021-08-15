import random

my_filledarray = [] * 2
my_emptyarray = ["Ford", "Ferrari", "Honda", "BMW", "Mustang"]

for x in my_emptyarray:
    print(x)


for y in range(10000):
    r = random.randint(1, 10000)
    if r == y:
        print("Matched!!  :" + str(y)) 
        break
    print(y)

"""
print("Enter the first name of car model: ")
my_emptyarray.append(input())

print(my_emptyarray)"""