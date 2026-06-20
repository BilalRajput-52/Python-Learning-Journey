# Chapter 5 - Dictionaries and Sets in Python

## Introduction

Dictionaries and Sets are important data structures in Python.

* Dictionary stores data in **key-value pairs**.
* Set stores **unique values** only.

---

# Dictionary in Python

## Definition

A Dictionary is a collection of key-value pairs.

Each value is accessed using its key.

---

# Creating a Dictionary

Example:

```python
student = {
    "name": "Bilal",
    "roll_no": "INFT232101052",
    "cgpa": 3.09
}
```

---

# Dictionary Structure

```python
student = {
    "name": "Bilal"
}
```

Here:

```text
Key   → name
Value → Bilal
```

---

# Accessing Values

Example:

```python
student = {
    "name": "Bilal",
    "cgpa": 3.09
}

print(student["name"])
```

---

# Using get()

Example:

```python
print(student.get("name"))
```

### Advantage

If key does not exist:

```python
print(student.get("age"))
```

Output:

```text
None
```

No error occurs.

---

# Updating Values

Example:

```python
student["cgpa"] = 3.50
```

---

# Adding New Key-Value Pair

Example:

```python
student["semester"] = "8th"
```

---

# Removing Items

## pop()

Example:

```python
student.pop("cgpa")
```

---

## del

Example:

```python
del student["cgpa"]
```

---

# Dictionary Methods

---

# keys()

Returns all keys.

Example:

```python
print(student.keys())
```

---

# values()

Returns all values.

Example:

```python
print(student.values())
```

---

# items()

Returns key-value pairs.

Example:

```python
print(student.items())
```

---

# update()

Adds or updates values.

Example:

```python
student.update({"cgpa": 3.50})
```

---

# clear()

Removes all items.

Example:

```python
student.clear()
```

---

# Nested Dictionary

## Definition

A dictionary inside another dictionary.

Example:

```python
students = {

    "student1": {
        "name": "Bilal",
        "cgpa": 3.09
    },

    "student2": {
        "name": "Ali",
        "cgpa": 3.50
    }
}
```

---

# Looping Through Dictionary

Example:

```python
for key, value in student.items():
    print(key, value)
```

---

# Important Notes About Dictionaries

* Dictionaries are mutable.
* Keys must be unique.
* Values can be duplicated.
* Dictionaries use curly braces `{}`.
* Data is stored as key-value pairs.

---

# Sets in Python

## Definition

A Set is an unordered collection of unique values.

---

# Creating a Set

Example:

```python
fruits = {"Apple", "Banana", "Mango"}
```

---

# Empty Set

Wrong:

```python
empty_set = {}
```

This creates a dictionary.

Correct:

```python
empty_set = set()
```

---

# Properties of Sets

## 1. Unordered

Sets do not maintain indexing positions.

Example:

```python
fruits = {"Apple", "Banana", "Mango"}
```

You cannot access:

```python
fruits[0]
```

This produces an error.

---

## 2. Unique Values

Duplicate values are automatically removed.

Example:

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

Result:

```text
{1, 2, 3, 4}
```

---

## 3. Mutable

Items can be added and removed.

Example:

```python
fruits.add("Orange")
```

---

## 4. Immutable Elements

Set items themselves must be immutable.

Allowed:

```python
{"Apple", "Banana"}
```

Not Allowed:

```python
{[1, 2, 3]}
```

Lists cannot be stored inside sets.

---

# Set Methods

---

# add()

Adds an item.

Example:

```python
fruits.add("Orange")
```

---

# remove()

Removes an item.

Example:

```python
fruits.remove("Apple")
```

---

# discard()

Removes an item without error.

Example:

```python
fruits.discard("Apple")
```

---

# pop()

Removes a random item.

Example:

```python
fruits.pop()
```

---

# clear()

Removes all items.

Example:

```python
fruits.clear()
```

---

# union()

Combines two sets.

Example:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
```

Result:

```text
{1, 2, 3, 4, 5}
```

---

# intersection()

Returns common values.

Example:

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.intersection(set2))
```

Result:

```text
{2, 3}
```

---

# difference()

Returns values present in first set but not in second.

Example:

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.difference(set2))
```

Result:

```text
{1}
```

---

# Membership Operators

Example:

```python
numbers = {1, 2, 3, 4}

print(2 in numbers)
```

---

# Frozen Set

## Definition

A Frozen Set is an immutable version of a set.

Example:

```python
numbers = frozenset([1, 2, 3])
```

Items cannot be changed.

---

# Dictionary vs Set

| Feature          | Dictionary     | Set         |
| ---------------- | -------------- | ----------- |
| Data Storage     | Key-Value Pair | Values Only |
| Mutable          | Yes            | Yes         |
| Duplicate Values | Values Allowed | Not Allowed |
| Indexing         | No             | No          |
| Syntax           | {}             | {}          |
| Empty Creation   | {}             | set()       |

---

# When to Use Dictionary?

Use Dictionary when data has labels.

Example:

```python
student = {
    "name": "Bilal",
    "cgpa": 3.09
}
```

---

# When to Use Set?

Use Set when unique values are required.

Example:

```python
unique_numbers = {1, 2, 3, 4}
```

---

# Important Notes

* Dictionaries store data using keys and values.
* Sets store unique values only.
* Dictionaries are mutable.
* Sets are mutable.
* Sets do not support indexing.
* Duplicate values are removed from sets.
* Dictionaries are best for structured data.
* Sets are best for uniqueness and mathematical operations.

---

# Summary

* Dictionary stores data in key-value pairs.
* Keys must be unique.
* Dictionary methods include keys(), values(), items(), get(), update(), and pop().
* Sets store unique values.
* Sets are unordered and do not support indexing.
* Set methods include add(), remove(), discard(), union(), intersection(), and difference().
* Dictionaries and Sets are powerful data structures used frequently in Python programs.