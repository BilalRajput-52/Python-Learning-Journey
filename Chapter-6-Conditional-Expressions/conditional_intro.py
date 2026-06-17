#  Conditional Expressions
 
# Conditional Expressions are used to make
# decisions in a program.

# The program checks a condition.
# If the condition is True, one block runs.
# If the condition is False, another block runs.

 
# 1. if Statement
 
# The if statement executes a block of code
# only when the condition is True.

age = 20

if age >= 18:
    print("You can vote.")

 
# 2. if-else Statement

# If the condition is True, the if block runs.
# Otherwise, the else block runs.

marks = 45

if marks >= 50:
    print("Pass")
else:
    print("Fail")

# 3. if-elif-else Statement

# Used when multiple conditions need
# to be checked.

score = 75

if score >= 80:
    print("Grade A")

elif score >= 70:
    print("Grade B")

else:
    print("Grade C")