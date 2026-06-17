student = {
    "name": "Bilal Ahmed",
    "reg_no": "INFT232101052",
    "university": "KFUEIT",
    "cgpa": 3.09
}

print("Student Information:")
print(student)

# Display all keys and values

print("\nDictionary Keys:")
print(student.keys())

print("\nDictionary Values:")
print(student.values())

# Update CGPA using update()
 

student.update({"cgpa": 3.20})

print("\nUpdated Dictionary:")
print(student)
