# Python program to create a tuple containing the names of 5 students and:

# Display the complete tuple.
# Display the first student.
# Display the last student.
# Display the total number of students .
# Display a slice containing the first 3 students.

# Creating a tuple of student names

students = (
    "Ali",
    "Bilal",
    "Ahmed",
    "Usman",
    "Hamza"
)

# Display complete tuple
print("Students Tuple:")
print(students)

# First student
print("\nFirst Student:")
print(students[0])

# Last student
print("\nLast Student:")
print(students[-1])

# Total students
print("\nTotal Students:")
print(len(students))

# First 3 students
print("\nFirst Three Students:")
print(students[0:3])

# Find how many times 10 occurs.
# Find the index of 30.
# Display the last element.
# Display the tuple in reverse order using slicing.


numbers = (10, 20, 30, 10, 40, 10)

print(numbers.count(10))
print(numbers.index(40))
print(numbers[-1])
print(numbers)
print(numbers[::-1])



age = 20

if not age == 18:
    print("not operator")