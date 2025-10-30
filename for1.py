# Example of using for loops in Python

# Loop from 0 to 9
for i in range(0, 10):
    print(i)

name = "Sagar"

# Loop through each character in the string
for n in name:
    print(n, end=" ")

print()  # new line for clean output

number = 10

# Loop from 1 to 9
for i in range(1, number):
    print(i)

li = [1, 'Sagar', 51]

# Loop through list elements
for l in li:
    print(l)

tup = (11, 21, "mango", 51, "Lemon")

# Loop through tuple elements
for t in tup:
    print(t)

dict1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

# Loop through dictionary keys and print key-value pairs
for x in dict1:
    print("%s : %d" % (x, dict1[x]))

set1 = {1, 2, 3, 4}

# Loop through set elements (order may vary)
for i in set1:
    print(i)

