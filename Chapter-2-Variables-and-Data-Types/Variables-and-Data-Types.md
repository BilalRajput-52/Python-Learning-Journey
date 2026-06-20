# Chapter 2 - Variables and Data Types in Python

## Introduction

Variables and Data Types are the foundation of Python programming.

A variable is used to store data in memory, while a data type defines the type of data stored in that variable.

---

# What is a Variable?

## Definition

A Variable is a name given to a memory location used to store data.

Variables act like containers that hold values.

Example:

```python
name = "Bilal"
age = 22
cgpa = 3.09
```

---

# Variable Naming Rules

1. Variable name can start with a letter (A-Z, a-z).
2. Variable name can start with an underscore (_).
3. Variable name cannot start with a number.
4. Spaces are not allowed in variable names.
5. Only letters, numbers, and underscores are allowed.
6. Special characters are not allowed.
7. Variable names are case-sensitive.
8. Variable names should be meaningful.
9. Python does not require explicit data type declaration.
10. Variable values can be changed during program execution.
11. Multiple variables can be created in one line.
12. Multiple variables can share the same value.
13. A variable should be assigned before use.
14. Python is a dynamically typed language.

---

# Identifiers

## Definition

Identifiers are names used for:

* Variables
* Functions
* Classes
* Objects

Example:

```python
student_name = "Bilal"
```

Here, `student_name` is an identifier.

---

# Keywords

## Definition

Keywords are reserved words in Python.

Examples:

```python
if
else
for
while
def
return
class
True
False
None
```

Keywords cannot be used as variable names.

Wrong:

```python
if = 10
```

---

# Data Types in Python

## Definition

A Data Type specifies the type of value stored in a variable.

---

# Integer (int)

Used to store whole numbers.

Example:

```python
age = 22
```

---

# Float (float)

Used to store decimal numbers.

Example:

```python
cgpa = 3.09
```

---

# String (str)

Used to store text.

Example:

```python
name = "Bilal"
```

---

# Boolean (bool)

Used to store True or False values.

Example:

```python
is_student = True
```

---

# None Type

Represents no value.

Example:

```python
data = None
```

---

# Checking Data Types

Python provides the type() function.

Example:

```python
name = "Bilal"

print(type(name))
```

---

# Type Casting

## Definition

Type Casting means converting one data type into another.

Example:

```python
age = "22"

age = int(age)
```

---

## Common Type Casting Functions

```python
int()
float()
str()
bool()
```

Example:

```python
num = "10"

print(int(num))
```

---

# Input Function

## Definition

The input() function is used to take input from the user.

Example:

```python
name = input("Enter your name: ")
```

---

# Taking Numeric Input

Example:

```python
num = int(input("Enter a number: "))
```

---

# Arithmetic Operators

## Definition

Arithmetic operators perform mathematical operations.

| Operator | Meaning        |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |
| %        | Modulus        |
| //       | Floor Division |
| **       | Exponent       |

Example:

```python
a = 10
b = 5

print(a + b)
```

---

# Assignment Operators

## Definition

Assignment operators assign values to variables.

Examples:

```python
=
+=
-=
*=
/=
```

Example:

```python
x = 10

x += 5
```

---

# Comparison Operators

## Definition

Comparison operators compare two values.

| Operator | Meaning               |
| -------- | --------------------- |
| ==       | Equal                 |
| !=       | Not Equal             |
| >        | Greater Than          |
| <        | Less Than             |
| >=       | Greater Than or Equal |
| <=       | Less Than or Equal    |

Example:

```python
print(10 > 5)
```

---

# Logical Operators

## Definition

Logical operators combine conditions.

| Operator | Meaning                     |
| -------- | --------------------------- |
| and      | Both conditions True        |
| or       | At least one condition True |
| not      | Reverse condition           |

Example:

```python
print(True and False)
```

---

# Comments in Python

## Definition

Comments are used to explain code.

Python ignores comments during execution.

Single-line Comment:

```python
# This is a comment
```

Multi-line Comment:

```python
"""
This is
a multi-line comment
"""
```

---

# Important Notes

* Python is case-sensitive.
* Variables do not require explicit type declaration.
* Data types can change during execution.
* Input always returns a string unless converted.

Example:

```python
age = 22

age = "Twenty Two"
```

This is valid in Python.

---

# Summary

* Variables store data.
* Data types define the type of data.
* Python supports int, float, str, bool, and None.
* type() checks data types.
* Type casting converts data from one type to another.
* input() takes user input.
* Operators perform calculations and comparisons.
* Comments improve code readability.
