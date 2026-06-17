 
#  Tuple Methods
 
# Definition:
# Since tuples are immutable, they have only a few methods.

# Common Tuple Methods:
#
# 1. count() -> Counts occurrences of a value.
# 2. index() -> Returns the first index of a value.

 
# Sample Tuple
 
numbers = (10, 20, 30, 10, 40, 10)

print("Tuple:")
print(numbers)

# count()
# Counts how many times a value appears.

print("\nCount Method:")

print(numbers.count(10))
print(numbers.count(20))

# index()
# Returns the index of the first occurrence.

print("\nIndex Method:")

print(numbers.index(10))
print(numbers.index(30))

# Example with Names
 
students = ("Ali", "Bilal", "Ahmed", "Bilal")

print("\nStudents Tuple:")
print(students)

print("\nCount of Bilal:")
print(students.count("Bilal"))

print("\nIndex of Ahmed:")
print(students.index("Ahmed"))