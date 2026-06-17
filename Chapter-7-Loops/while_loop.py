# Topic: While Loop

# Definition:

# A while loop executes a block of code

# repeatedly as long as the condition remains True.

# Syntax:

# while condition:
    # code

# Example 1

# Print Numbers from 1 to 5

i = 1

while i <= 5:
   print(i)
i += 1

# Example 2

# Print a Message Multiple Times
 
count = 1

while count <= 3:
    print("Welcome to Python")
count += 1

# Example 3

# User Input Example

num = int(input("Enter a number: "))

i = 1

while i <= num:
    print(i)
i += 1

# Example 4

# Print Even Numbers
 
i = 2

while i <= 10:
   print(i)
i += 2
 
# Example 5

# Countdown
 

i = 5

while i >= 1:
   print(i)
i -= 1

# Important Note

# Always update the loop variable.

# Example:

# i = 1
# while i <= 5:
   # print(i)

# This creates an Infinite Loop because
# i never changes.
# ==========================================

# Correct:
# i = 1
# while i <= 5:
   # print(i)
# i += 1

# The loop stops when the condition becomes False.

# Key Points
# while loop condition par kaam karta hai.
# Jab tak condition True rahegi, loop chalta rahega.
# Loop variable ko update karna zaroori hai.
# i += 1 increment kehlata hai.
# i -= 1 decrement kehlata hai.