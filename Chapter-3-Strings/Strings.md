# Chapter 3 - Strings in Python

## Introduction

Strings are one of the most commonly used data types in Python.

A String is used to store text data such as names, messages, addresses, and sentences.

---

# What is a String?

## Definition

A String is a sequence of characters enclosed in quotes.

A string can be written using:

* Single Quotes (' ')
* Double Quotes (" ")
* Triple Quotes (''' ''' or """ """)

Example:

```python
name = "Bilal"
course = 'Python'
message = """Welcome to Python"""
```

---

# Creating Strings

Example:

```python
name = "Bilal"
city = "Rahim Yar Khan"
course = "Python Programming"
```

---

# Accessing Characters in a String

Characters in a string can be accessed using indexing.

Example:

```python
name = "Bilal"

print(name[0])
print(name[1])
print(name[2])
```

---

# String Indexing

## Definition

Indexing is used to access a single character from a string.

Example:

```python
name = "Bilal"
```

| Character | B | i | l | a | l |
| --------- | - | - | - | - | - |
| Index     | 0 | 1 | 2 | 3 | 4 |

Example:

```python
print(name[0])
print(name[3])
```

---

# Negative Indexing

Python also supports negative indexing.

Example:

```python
name = "Bilal"
```

| Character | B  | i  | l  | a  | l  |
| --------- | -- | -- | -- | -- | -- |
| Index     | -5 | -4 | -3 | -2 | -1 |

Example:

```python
print(name[-1])
print(name[-2])
```

---

# String Slicing

## Definition

Slicing is used to get a portion of a string.

Syntax:

```python
string[start:end]
```

Important Rule:

```text
Start Index  → Included
End Index    → Excluded
```

Example:

```python
name = "Bilal"

print(name[0:3])
```

Result:

```text
Bil
```

---

# Common Slicing Examples

Example:

```python
name = "Bilal"

print(name[0:3])
print(name[1:4])
print(name[:3])
print(name[2:])
print(name[:])
```

Explanation:

```text
name[0:3] → Bil
name[1:4] → ila
name[:3]  → Bil
name[2:]  → lal
name[:]   → Complete String
```

---

# Skip Slicing

## Definition

Skip slicing allows us to skip characters while slicing.

Syntax:

```python
string[start:end:step]
```

Example:

```python
name = "Bilal"

print(name[0:5:2])
```

Result:

```text
Bla
```

Explanation:

```text
Start = 0
End = 5
Step = 2

B → l → l
```

---

# String Functions

Python provides many built-in string functions.

---

# len()

Returns the length of a string.

Example:

```python
name = "Bilal"

print(len(name))
```

---

# endswith()

Checks whether a string ends with a specific value.

Example:

```python
name = "Bilal"

print(name.endswith("al"))
```

---

# startswith()

Checks whether a string starts with a specific value.

Example:

```python
name = "Bilal"

print(name.startswith("Bi"))
```

---

# count()

Counts occurrences of a character or word.

Example:

```python
name = "Bilal"

print(name.count("l"))
```

---

# capitalize()

Converts the first character to uppercase.

Example:

```python
name = "bilal"

print(name.capitalize())
```

---

# title()

Converts the first letter of each word to uppercase.

Example:

```python
text = "python programming"

print(text.title())
```

---

# upper()

Converts all characters to uppercase.

Example:

```python
name = "Bilal"

print(name.upper())
```

---

# lower()

Converts all characters to lowercase.

Example:

```python
name = "BILAL"

print(name.lower())
```

---

# find()

Returns the index of the first occurrence.

Example:

```python
name = "Bilal"

print(name.find("a"))
```

---

# replace()

Replaces one value with another.

Example:

```python
name = "Bilal"

print(name.replace("Bilal", "Ahmed"))
```

---

# Escape Sequence Characters

## Definition

Escape Sequence Characters are special characters that start with a backslash ().

They are used for formatting and displaying special characters.

---

# Common Escape Sequences

| Escape Sequence | Meaning      |
| --------------- | ------------ |
| \n              | New Line     |
| \t              | Tab Space    |
| "               | Double Quote |
| '               | Single Quote |
| \               | Backslash    |

---

# Examples

## New Line

```python
print("Hello\nWorld")
```

---

## Tab Space

```python
print("Name:\tBilal")
```

---

## Double Quotes

```python
print("\"Welcome to Python\"")
```

---

## Backslash

```python
print("C:\\Users\\Bilal")
```

---

# Strings are Immutable

## Definition

Strings are immutable in Python.

This means:

```text
A string cannot be changed after it is created.
```

---

# Wrong Example

```python
name = "Bilal"

name[0] = "M"
```

This will generate an error.

---

# Correct Way

```python
name = "Bilal"

new_name = "M" + name[1:]

print(new_name)
```

Result:

```text
Milal
```

---

# Detecting Double Spaces

Example:

```python
text = "Hello  Bilal"

print(text.find("  "))
```

If the result is:

```text
-1
```

No double spaces exist.

Otherwise, the returned index shows where double spaces are located.

---

# Important Notes

* Strings are ordered collections.
* Strings support indexing.
* Strings support slicing.
* Strings are immutable.
* Strings can contain letters, numbers, symbols, and spaces.
* Python provides many built-in string methods.

---

# Summary

* Strings store text data.
* Indexing accesses a single character.
* Slicing extracts a portion of a string.
* Skip slicing skips characters using a step value.
* String methods perform common operations.
* Escape sequences provide special formatting.
* Strings are immutable and cannot be modified directly.
* New strings must be created when changes are required.