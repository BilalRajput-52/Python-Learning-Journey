# Chapter 6 - Conditional Expressions in Python

## Introduction

Conditional statements are used to make decisions in a program.

They allow a program to execute different blocks of code based on different conditions.

Without conditional statements, a program would execute all statements sequentially without making decisions.

---

# What is a Conditional Expression?

## Definition

A Conditional Expression is an expression that evaluates to either:

```text
True
False
```

Python uses these conditions to decide which block of code should execute.

Example:

```python
age = 20

print(age >= 18)
```

---

# Comparison Operators

## Definition

Comparison operators compare two values and return either True or False.

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal To                 |
| !=       | Not Equal To             |
| >        | Greater Than             |
| <        | Less Than                |
| >=       | Greater Than or Equal To |
| <=       | Less Than or Equal To    |

Example:

```python
a = 10
b = 20

print(a < b)
```

---

# if Statement

## Definition

The if statement executes a block of code only when the condition is True.

## Syntax

```python
if condition:
    code
```

## Example

```python
age = 20

if age >= 18:
    print("You can vote.")
```

---

# Flow of if Statement

```text
Condition True  → Execute Code

Condition False → Skip Code
```

---

# if-else Statement

## Definition

The else block executes when the if condition is False.

## Syntax

```python
if condition:
    code

else:
    code
```

## Example

```python
age = 16

if age >= 18:
    print("You can vote.")

else:
    print("You cannot vote.")
```

---

# Flow of if-else

```text
Condition True  → if Block

Condition False → else Block
```

---

# if-elif-else Statement

## Definition

Used when multiple conditions need to be checked.

## Syntax

```python
if condition:
    code

elif condition:
    code

else:
    code
```

## Example

```python
marks = 75

if marks >= 90:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

else:
    print("Grade C")
```

---

# Working of if-elif-else

Python checks conditions from top to bottom.

The first True condition executes.

Remaining conditions are ignored.

Example:

```text
Condition 1 → False

Condition 2 → True

Execute Condition 2 Block

Stop Checking
```

---

# Logical Operators

## Definition

Logical operators combine multiple conditions.

---

# and Operator

Returns True only if all conditions are True.

Example:

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible")
```

---

# or Operator

Returns True if at least one condition is True.

Example:

```python
marks = 85

if marks >= 90 or marks >= 80:
    print("Passed")
```

---

# not Operator

Reverses the condition.

Example:

```python
is_logged_in = False

if not is_logged_in:
    print("Please Login")
```

---

# Nested if Statement

## Definition

An if statement inside another if statement is called a Nested if Statement.

## Syntax

```python
if condition:

    if condition:
        code
```

## Example

```python
age = 20
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to Vote")
```

---

# Real-World Example

## ATM Withdrawal

```python
balance = 5000
amount = 2000

if amount <= balance:
    print("Withdrawal Successful")

else:
    print("Insufficient Balance")
```

---

# Real-World Example

## Student Result

```python
marks = 85

if marks >= 50:
    print("Pass")

else:
    print("Fail")
```

---

# Real-World Example

## Login System

```python
username = "Bilal"
password = "1234"

if username == "Bilal" and password == "1234":
    print("Login Successful")

else:
    print("Invalid Credentials")
```

---

# Ternary Conditional Expression

## Definition

A short form of if-else.

## Syntax

```python
value_if_true if condition else value_if_false
```

## Example

```python
age = 20

message = "Adult" if age >= 18 else "Minor"

print(message)
```

---

# Important Notes

* Every if statement requires a condition.
* Conditions must evaluate to True or False.
* Python uses indentation to define blocks.
* Only one block of an if-elif-else chain executes.
* Nested if statements are used for complex decisions.
* Logical operators help combine conditions.
* Ternary expressions provide a short form of if-else.

---

# Common Mistakes

## Missing Colon

Wrong:

```python
if age >= 18
    print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## Incorrect Indentation

Wrong:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

# Summary

* Conditional statements help programs make decisions.
* if executes code when a condition is True.
* else executes code when a condition is False.
* if-elif-else is used for multiple conditions.
* Comparison operators return True or False.
* Logical operators combine conditions.
* Nested if statements allow complex decision-making.
* Ternary expressions provide a short form of if-else.
* Indentation is extremely important in Python.