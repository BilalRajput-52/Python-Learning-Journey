 
#  Indexing and Slicing

students = ["Ali", "Bilal", "Ahmed", "Usman"]

print("Original List:")
print(students)

# Positive Indexing
 
print("\n Positive Indexing")

print(students[0])
print(students[1])
print(students[2])
 
# Negative Indexing
 
print("\n Negative Indexing ")

print(students[-1])
print(students[-2])

# List Slicing
 
print("\n List Slicing ")

print(students[0:2])
print(students[1:3])

# Missing Values
 

print("\nMissing Values")

print(students[:2])
print(students[2:])
print(students[:])

# Skip Slicing
 

print("\nSkip Slicing ")

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0:6:2])

 
# Reverse List
 
print("\n Reverse List")

print(numbers[::-1])