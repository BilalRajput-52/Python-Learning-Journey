 

# Chapter 3 - Strings in Python

# Topic: Indexing and Slicing


# String Example

name = "BilalAhmed"

print("Original String:", name)

 

# 1. Positive Indexing


# Indexing is used to access a single character.

# B  i  l  a  l  A  h  m  e  d

# 0  1  2  3  4  5  6  7  8  9

print(" Positive Indexing ")

print("First Character  :", name[0])
print("Second Character :", name[1])
print("Third Character  :", name[2])


# 2. Negative Indexing

 

# B  i  l  a  l  A  h  m  e  d

# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print("\n--- Negative Indexing ---")

print( name[-8])
print( name[-6])
print( name[-3])
 

# 3. String Slicing


# Syntax:

# string[start : end]

# Start Index = Included

# End Index   = Excluded

print("\n--- String Slicing ---")

print(name[0:5])   # Bilal
print(name[5:10])  # Ahmed
print(name[2:7])   # lalAh


# 4. Slicing with Missing Values

 

print(" Slicing with Missing Values")

print(name[:5])    # Start from 0
print(name[5:])    # Go till end
print(name[:])     # Complete String

 

# 5. Skip Slicing (Step Value)

 

# Syntax:

# string[start:end:step]

print("\n--- Skip Slicing ---")

print(name[0:10:2])   # Every 2nd character
print(name[0:6:2])   # Every 3rd character

 

# 6. Reverse String

 

print("  Reverse String ")

print(name[::-1])

 

# 7. String Length

 

print("Length of String ")

print("Length =", len(name))
