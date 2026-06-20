# Chapter 4 - Lists and Tuples in Python

## Introduction

Lists and Tuples are used to store multiple values in a single variable.

Instead of creating many variables, we can store related data together using Lists or Tuples.

---

# Lists in Python

## Definition

A List is an ordered and mutable collection of items.

### Ordered

Items maintain their position.

### Mutable

Items can be changed after creation.

---

# Creating a List

Example:

```python
students = ["Bilal", "Ali", "Ahmed"]
```

Example:

```python
numbers = [10, 20, 30, 40]
```

---

# List Can Store Different Data Types

Example:

```python
data = ["Bilal", 22, 3.09, True]
```

---

# Accessing List Elements

Lists use indexing.

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
```

---

# Negative Indexing

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[-1])
print(fruits[-2])
```

---

# List Slicing

## Definition

Slicing is used to get a portion of a list.

Syntax:

```python
list[start:end]
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

---

# Skip Slicing

Syntax:

```python
list[start:end:step]
```

Example:

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0:6:2])
```

---

# Updating List Elements

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"
```

Lists are mutable, so values can be changed.

---

# List Methods

Python provides many built-in list methods.

---

# append()

Adds an item at the end.

Example:

```python
fruits.append("Orange")
```

---

# insert()

Adds an item at a specific index.

Example:

```python
fruits.insert(1, "Orange")
```

---

# remove()

Removes a specific item.

Example:

```python
fruits.remove("Banana")
```

---

# pop()

Removes an item using its index.

Example:

```python
fruits.pop(1)
```

---

# sort()

Sorts the list in ascending order.

Example:

```python
marks = [78, 91, 85, 69]

marks.sort()
```

Important:

```python
marks.sort()

print(marks)
```

Correct

```python
arrange = marks.sort()

print(arrange)
```

Wrong because sort() returns None.

---

# reverse()

Reverses the list.

Example:

```python
numbers.reverse()
```

---

# count()

Counts occurrences of an item.

Example:

```python
numbers.count(10)
```

---

# index()

Returns the index of an item.

Example:

```python
numbers.index(30)
```

---

# copy()

Creates a copy of a list.

Example:

```python
new_list = numbers.copy()
```

---

# Length of List

Example:

```python
print(len(numbers))
```

---

# Nested Lists

## Definition

A list inside another list is called a nested list.

Example:

```python
data = [
    ["Bilal", 22],
    ["Ali", 21]
]
```

---

# Tuples in Python

## Definition

A Tuple is an ordered and immutable collection of items.

### Ordered

Items maintain their position.

### Immutable

Items cannot be changed after creation.

---

# Creating a Tuple

Example:

```python
coordinates = (4, 5)
```

---

# Mixed Data Types

Example:

```python
user_profile = ("Bilal", 22, True)
```

---

# Single Item Tuple

Important:

```python
single_item = (42,)
```

Without comma:

```python
single_item = (42)
```

Python treats it as an integer.

---

# Checking Tuple Type

Example:

```python
coordinates = (4, 5)

print(type(coordinates))
```

---

# Tuple Indexing

Example:

```python
student = ("Bilal", "KFUEIT", 3.09)

print(student[0])
```

---

# Tuple Slicing

Example:

```python
student = ("Bilal", "KFUEIT", 3.09)

print(student[0:2])
```

---

# Tuples are Immutable

Wrong:

```python
student[0] = "Ahmed"
```

This generates an error.

---

# Tuple Methods

Tuples have very few methods.

---

# count()

Counts occurrences of a value.

Example:

```python
numbers = (1, 2, 3, 1)

print(numbers.count(1))
```

---

# index()

Returns the first occurrence index.

Example:

```python
numbers = (10, 20, 30)

print(numbers.index(20))
```

---

# Tuple Operations

---

# Concatenation

Combining tuples.

Example:

```python
tuple1 = (1, 2)
tuple2 = (3, 4)

result = tuple1 + tuple2
```

---

# Repetition

Repeating tuple values.

Example:

```python
numbers = (1, 2)

print(numbers * 3)
```

---

# Membership Operators

Checking whether a value exists.

Example:

```python
numbers = (10, 20, 30)

print(20 in numbers)
```

---

# Packing and Unpacking

## Packing

```python
student = ("Bilal", 22, 3.09)
```

---

## Unpacking

```python
name, age, cgpa = student
```

---

# List vs Tuple

| Feature     | List   | Tuple  |
| ----------- | ------ | ------ |
| Ordered     | Yes    | Yes    |
| Mutable     | Yes    | No     |
| Indexing    | Yes    | Yes    |
| Slicing     | Yes    | Yes    |
| Methods     | Many   | Few    |
| Performance | Slower | Faster |

---

# When to Use Lists?

Use Lists when data may change.

Example:

```python
shopping_list = ["Milk", "Bread"]
```

---

# When to Use Tuples?

Use Tuples when data should remain fixed.

Example:

```python
coordinates = (10, 20)
```

---

# Important Notes

* Lists are mutable.
* Tuples are immutable.
* Both support indexing.
* Both support slicing.
* Lists have many methods.
* Tuples have only a few methods.
* Lists use square brackets [].
* Tuples use parentheses ().

---

# Summary

* Lists store multiple values and can be modified.
* Tuples store multiple values but cannot be modified.
* Lists support append(), insert(), remove(), pop(), sort(), and more.
* Tuples mainly support count() and index().
* Both support indexing and slicing.
* Lists are used for dynamic data.
* Tuples are used for fixed data.