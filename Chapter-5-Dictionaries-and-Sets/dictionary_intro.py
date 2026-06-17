 # Chapter 5 - Dictionaries in Python
 
# Definition:
# A dictionary is a collection of key-value pairs.
# Dictionaries are enclosed in curly braces {}.
# Dictionaries are mutable.
# Dictionary stores data in key-value pairs.
# Keys must be unique.
# Values can be duplicated.

student = {
    "name": "Bilal Ahmed",
    "reg_no": "INFT232101052",
    "university": "KFUEIT",
    "city": "Rahim Yar Khan",
    "cgpa": 3.09
    
}

print("Student Dictionary:")
print(student,type(student))

# Accessing Values

print("\nStudent Name:")
print(student["name"])

print("\nCGPA:")
print(student["cgpa"])

# Updating Value

student["cgpa"] = 3.20

print("\nUpdated CGPA:")
print(student["cgpa"])

# Adding New Key

student["semester"] = "8th"

print("\nAfter Adding Semester:")
print(student["semester"])

print(student)