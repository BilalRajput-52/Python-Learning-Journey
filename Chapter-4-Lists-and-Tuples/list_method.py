 
 
#   List Methods
 

# Definition:
# List Methods are built-in functions that are used
# to perform operations on lists such as adding,
# removing, sorting, and modifying elements.

 
# Commonly Used List Methods
 
# 1. append()  -> Adds an item at the end of the list.
# 2. insert()  -> Adds an item at a specific position.
# 3. pop()     -> Removes an item using its index.
# 4. remove()  -> Removes an item using its value.
# 5. sort()    -> Sorts the list in ascending order.
# 6. reverse() -> Reverses the order of the list.

 
# Original List
 
students = ["Ali", "Bilal", "Ahmed"]

print("Original List:")
print(students)

# append()
# Adds an item at the end of the list.

students.append("Usman")

print("\nAfter append():")
print(students)

# insert()
# Adds an item at a specific index.

students.insert(1, "Hamza")

print("\nAfter insert():")
print(students)

# pop()
# Removes an item using its index.

students.pop(2)

print("\nAfter pop():")
print(students)

# remove()
# Removes an item using its value.

students.remove("Ahmed")

print("\nAfter remove():")
print(students)

# sort()
# Sorts the list in ascending order.

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print("\nAfter sort():")
print(numbers)


# reverse()
# Reverses the order of the list.

numbers.reverse()

print("\nAfter reverse():")
print(numbers)


# num1 = [50, 10, 40, 20, 30]
# num1.append(333) 
# print(num1)

"""list.append(value)
list.insert(index, value)
list.pop(index)
list.remove(value)
list.sort()
list.reverse()"""