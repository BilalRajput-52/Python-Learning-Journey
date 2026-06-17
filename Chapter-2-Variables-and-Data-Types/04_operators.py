# there are  four operators in python programming language 

# Arithmetic: + - * / % ** //

# Assignment: = += -= *= /=

# Comparison: == != > < >= <=

# Logical: and or not

 
                                    # PYTHON OPERATORS
 
# 1. Arithmetic Operators
# Arithmetic operators are used to perform mathematical calculations
# such as addition, subtraction, multiplication, division, etc.

a = 10
b = 5

print("Arithmetic Operators")
print("Addition:", a + b)         # +
print("Subtraction:", a - b)      # -
print("Multiplication:", a * b)   # *
print("Division:", a / b)         # /
print("Modulus:", a % b)          # %
print("Power:", a ** b)           # **
print("Floor Division:", a // b)  # //
print()

# 2. Assignment Operators
# Assignment operators are used to assign values to variables.

x = 10       # Assign value 10 to x
x += 5       # x = x + 5

print("Assignment Operators")
print("After += :", x)

x -= 3       # x = x - 3

print("After -= :", x)

x *= 2       # x = x * 2

print("After *= :", x)

print()


# 3.Comparison Operators
# Definition:
# Comparison operators are used to compare two values.
# They always return True or False.

num1 = 10
num2 = 20

print("Comparison Operators")
print("Equal to:", num1 == num2)          # ==
print("Not Equal to:", num1 != num2)      # !=
print("Greater than:", num1 > num2)       # >
print("Less than:", num1 < num2)          # <
print("Greater or Equal:", num1 >= num2)  # >=
print("Less or Equal:", num1 <= num2)     # <=

print()


# 4.Logical Operators
# Definition:
# Logical operators are used to combine multiple conditions.

age = 20
student = True

print("Logical Operators")

# AND operator
print(age > 18 and student)

# OR operator
print(age > 25 or student)

# NOT operator
print(not (student))
print(not(True))