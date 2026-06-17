 
# Chapter 5 - Sets in Python

# Definition:
# A set is an unordered collection of unique items.
# Sets are enclosed in curly braces {}.
# Set

# Uses {}
# Unordered
# Unique values only
# Mutable
# No indexing
# No slicing
# Duplicates are automatically removed
# Creating a Set

fruits = {"Apple", "Banana", "Mango"}

print("Set:")
print(fruits)

# Duplicate Values

numbers = {10, 20, 30, 20, 10}

print("\nDuplicates Removed:")
print(numbers)

# Adding an Element

numbers.add(40)

print("\nAfter Adding 40:")
print(numbers)

# Different Data Types
 
data = {10, "Bilal", 3.09, True}

print("\nMixed Data Types:")
print(data)

# Empty Set
 
empty_set = set()

print("\nType of Empty Set:")
print(type(empty_set))

 
# Empty Dictionary

empty_dict = {}

print("\nType of Empty Dictionary:")
print(type(empty_dict))