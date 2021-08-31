import array

unsorted = [384, 201, 34, 1, 432, 23, 89, 719, 24]

for x in unsorted:
    print(x)

print("===============================")
unsorted.append(555)
unsorted.sort()
for x in range(len(unsorted)):
    print(unsorted[x]) 