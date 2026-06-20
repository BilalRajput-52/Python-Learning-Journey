# Chapter 7 - Loops in Python

## Introduction

Loops are used to execute a block of code repeatedly.

Instead of writing the same code multiple times, we can use loops to perform repetitive tasks efficiently.

Python provides two main types of loops:

1. while Loop
2. for Loop

---

# What is a Loop?

## Definition

A Loop is a programming structure that repeats a block of code until a specified condition is met.

Example:

```python
for i in range(5):
    print("Hello")
```

Instead of writing:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

---

# while Loop

## Definition

A while loop executes as long as its condition remains True.

## Syntax

```python
while condition:
    code
```

---

# Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# Working

```text
Condition True  → Execute Loop

Condition False → Stop Loop
```

---

# Infinite Loop

## Definition

A loop that never ends is called an Infinite Loop.

Example:

```python
while True:
    print("Hello")
```

⚠ Use carefully because it runs forever.

---

# for Loop

## Definition

A for loop is used to iterate over a sequence.

A sequence can be:

* List
* Tuple
* String
* Range

---

# Syntax

```python
for variable in sequence:
    code
```

---

# Example

```python
for i in range(5):
    print(i)
```

---

# Working

```text
Take First Value
Execute Code

Take Next Value
Execute Code

Continue Until Sequence Ends
```

---

# range() Function

## Definition

The range() function generates a sequence of numbers.

---

# range(stop)

Example:

```python
for i in range(5):
    print(i)
```

Output Values:

```text
0
1
2
3
4
```

---

# range(start, stop)

Example:

```python
for i in range(1, 6):
    print(i)
```

Output Values:

```text
1
2
3
4
5
```

---

# range(start, stop, step)

Example:

```python
for i in range(0, 10, 2):
    print(i)
```

Output Values:

```text
0
2
4
6
8
```

---

# break Statement

## Definition

The break statement immediately terminates the loop.

---

# Example

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

---

# Working

```text
Loop Runs

i becomes 5

break Executes

Loop Stops
```

---

# continue Statement

## Definition

The continue statement skips the current iteration and moves to the next iteration.

---

# Example

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

---

# Working

```text
i = 2

continue Executes

Current Iteration Skipped

Next Iteration Starts
```

---

# pass Statement

## Definition

The pass statement does nothing.

It is used as a placeholder.

---

# Example

```python
for i in range(5):
    pass
```

---

# Why Use pass?

Sometimes a block is required syntactically but no code has been written yet.

Example:

```python
if True:
    pass
```

---

# Nested Loops

## Definition

A loop inside another loop is called a Nested Loop.

---

# Example

```python
for row in range(3):

    for column in range(3):
        print("*", end=" ")

    print()
```

---

# Working

Outer Loop:

```text
Controls Rows
```

Inner Loop:

```text
Controls Columns
```

---

# Loops with Lists

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

---

# Loops with Tuples

Example:

```python
students = ("Bilal", "Ali", "Ahmed")

for student in students:
    print(student)
```

---

# Loops with Strings

Example:

```python
name = "Bilal"

for character in name:
    print(character)
```

---

# Using else with Loops

## Definition

The else block executes when the loop completes normally.

---

# Example

```python
for i in range(5):
    print(i)

else:
    print("Loop Finished")
```

---

# Example with while

```python
count = 1

while count <= 5:
    print(count)
    count += 1

else:
    print("Loop Finished")
```

---

# Pattern Printing Basics

Pattern printing is one of the best ways to learn loops.

---

# Square Pattern

```text
*****
*****
*****
*****
*****
```

Logic:

```python
for row in range(5):

    for column in range(5):
        print("*", end="")

    print()
```

---

# Right Triangle Pattern

```text
*
**
***
****
*****
```

Logic:

```python
for row in range(1, 6):

    for column in range(row):
        print("*", end="")

    print()
```

---

# Inverted Triangle Pattern

```text
*****
****
***
**
*
```

Logic:

```python
for row in range(5, 0, -1):

    for column in range(row):
        print("*", end="")

    print()
```

---

# Common Use Cases of Loops

Loops are commonly used for:

* Traversing Lists
* Traversing Tuples
* Traversing Strings
* Pattern Printing
* Data Processing
* Searching
* Counting
* Repetitive Tasks

---

# Important Notes

* while loop depends on a condition.
* for loop depends on a sequence.
* range() is commonly used with for loops.
* break stops a loop immediately.
* continue skips the current iteration.
* pass acts as a placeholder.
* Nested loops are useful for patterns and tables.
* Loops can iterate through lists, tuples, and strings.

---

# Common Mistakes

## Infinite Loop

Wrong:

```python
count = 1

while count <= 5:
    print(count)
```

Reason:

```text
count never changes
```

Correct:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Wrong Indentation

Wrong:

```python
for i in range(5):
print(i)
```

Correct:

```python
for i in range(5):
    print(i)
```

---

# Summary

* Loops execute code repeatedly.
* Python provides while and for loops.
* range() generates number sequences.
* break exits a loop immediately.
* continue skips the current iteration.
* pass is a placeholder statement.
* Nested loops are loops inside loops.
* Loops can iterate through lists, tuples, and strings.
* Pattern printing is one of the best applications of loops.
* Loops help reduce code repetition and improve efficiency.