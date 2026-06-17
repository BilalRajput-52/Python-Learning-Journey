
#   Tuples in Python
 
# Definition:
# A tuple is an ordered collection of items.
# Tuples are enclosed in parentheses ().
# Tuples are immutable, meaning they cannot be changed.
"""
Important Points for Exams
Tuple uses parentheses ().
Tuple is ordered.
Tuple supports indexing.
Tuple supports slicing.
Tuple is immutable.
Common methods:
count()
index()
Single element tuple requires a comma:  num=(675,)
"""

 
# Standard Tuple Creation

coordinates = (4, 5)

print(coordinates)

# Tuples Can Store Mixed Data Types
 
user_profile = ("Bilal Ahmed", 22, True, 3.09)

print(user_profile)

# Creating a Single Item Tuple

single_item = (42,)

print(single_item)

# Verifying Data Type
 
print(type(coordinates))
print(type(single_item))

# Example Tuple
 
school = (
    "Bilal Ahmed",
    "INFT232101052",
    "KFUEIT",
    "Rahim Yar Khan",
    " 3.09",
    " 8th"
)

print("\nSchool Information:")
print(school)

# Tuple Indexing

print("\nStudent Name :", school[0])
print("Registration :", school[1])
print("University   :", school[2])
print(" City        :", school[3])
print(" Semester    :", school[5])
print(" CGPA        :", school[4])

# Tuples are Immutable
 

# The following code will generate an error:

# school[0] = "BILAL"

# Error:
# TypeError: 'tuple' object does not support item assignment

# We cannot modify, replace, or change tuple elements.


list = list(input("user entering a list  :"))
print("List is :", list)
