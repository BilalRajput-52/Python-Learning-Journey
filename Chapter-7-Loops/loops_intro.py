# A Loop is used to execute a block of code repeatedly.

# Agar humein ek hi kaam multiple times karna ho, 
# to hum loops use karte hain.

# Without Loop
print("Bilal")
print("Bilal")
print("Bilal")
print("Bilal")
print("Bilal")

# With Loop
for i in range(5):
    print("Bilal")

    # Same result, lekin code bohat chhota aur clean ho gaya.

"""
Why Use Loops?

Repeating tasks
Printing tables
Traversing Lists
Traversing Tuples
Traversing Strings
Taking multiple inputs
Data processing
"""
# Types of Loops in Python
# 1. while Loop

# while condition:
#     code
#============================
# 2. for Loop
# for item in range():
#     code
#==================================

# 1. While Loop
# Definition

# A while loop tab tak chalta rehta hai jab tak condition True rahe.

# Syntax
# while condition:
#     code
# Example
#====================================
i = 1

while i <= 5:
    print(i)
    i += 1
#=====================================
# Infinite Loop
 
# i = 1

# while i <= 5:
#     print(i)

# Problem:

# i kabhi increase nahi ho raha.

# Condition hamesha True rahegi.

# Program kabhi stop nahi hoga.

# Isay Infinite Loop kehte hain.
# ================================================

# 2. For Loop
# Definition

# A for loop sequence ke har item par iterate karta hai.

# Syntax
# for item in sequence:
#     code
 
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
# =======================================================
# Using range()
# range() numbers ki sequence generate karta hai.
i=1
for i in range(5):
    print(i)
# ===========================================

# Difference Between While and For

# | While Loop                   | For Loop                     |
# | ---------------------------- | ---------------------------- |
# | Runs on a condition          | Runs on a sequence           |
# | Manual increment needed      | Automatic iteration          |
# | Can become infinite          | Less chance of infinite loop |
# | Best for unknown repetitions | Best for known repetitions   |

#=======================================================================