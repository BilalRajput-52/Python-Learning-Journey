 
#  Dictionary Methods
 

student = {
    "name": "Bilal Ahmed",
    "reg_no": "INFT232101052",
    "cgpa": 3.09,
    "semester": "8th"
}

print("Original Dictionary:")
print(student)

# keys()
# Returns all keys of the dictionary.

print("\nKeys:")
print(student.keys())

# values()
# Returns all values of the dictionary.

print("\nValues:")
print(student.values())

# items()
# Returns key-value pairs as tuples.

print("\nItems:")
print(student.items())

# get()
# Returns value of a key.

print("\nGet Method:")
print(student.get("name"))

# update()
# Updates existing key or adds new key.

student.update({"cgpa": 3.20})

print("\nAfter Update:")
print(student)

# pop()
# Removes a key from the dictionary.

student.pop("semester")

print("\nAfter Pop:")
print(student)


num=()
print(type(num))