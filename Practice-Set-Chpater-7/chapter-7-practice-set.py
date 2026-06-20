# Practice Set
 
# Question 1
# Print numbers from 1 to 50 using a while loop.

i = 1

while i <= 50:
    print(i)
    i += 1

# Question 2
# Print numbers from 1 to 10 using a for loop.

for i in range(1, 11):
    print(i)

# Question 3
# Print the multiplication table of 5.

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Question 4
# Print all items of a list using a loop.

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

# Question 5
# Print each character of a string.

name = "Bilal"

for character in name:
    print(character)

# Question 6
# Print even numbers from 2 to 20.

for i in range(2, 21, 2):
    print(i)

# Question 7
# Print numbers from 10 to 1.

for i in range(10, 0, -1):
    print(i)

# Question 8
# Use break to stop a loop at 5.

for i in range(1, 11):

    if i == 5:
        break

    print(i)

# Question 9
# Use continue to skip number 5.

for i in range(1, 11):

    if i == 5:
        continue

    print(i)

# Question 10
# Find the sum of numbers from 1 to 10.

total = 0

for i in range(1, 11):
    total += i

print(total)