""" Python Variables ke tamam important rules ki list:

1 Variable name letter (A-Z, a-z) se start ho sakta hai.
2 Variable name underscore (_) se start ho sakta hai.
3 Variable name number (0-9) se start nahi ho sakta.
4 Variable name mein spaces allowed nahi hain.
5 Variable name mein sirf letters, numbers aur underscore (_) use ho sakte hain.
6 Special characters allowed nahi hain, jaise:@ # $ % & - ! *
7 Variable names case-sensitive hote hain.
name, Name, aur NAME teen alag variables hain.
8 Variable ki length par practically koi chhoti limit nahi hai, lekin naam readable hona chahiye.
9 Variable name meaningful aur descriptive hona chahiye.
10 Python mein variable declare karne ke liye data type likhna zaroori nahi hota.
11 Variable ki value program ke dauran change ki ja sakti hai.
12 Ek hi line mein multiple variables create kiye ja sakte hain.
13 Ek hi value multiple variables ko assign ki ja sakti hai.
14 Variable ko use karne se pehle uski value assign honi chahiye.
15 Python dynamically typed language hai, is liye ek variable ki type baad mein change ho sakti hai.



"""




# Python Variable Naming Rules Example
 

# Rule 1: Start with letter
name = "Bilal"

# Rule 1: Start with underscore
_age = 21

# Rule 2: Cannot start with number
# 1name = "Bilal"      # Invalid

# Rule 3: No spaces allowed
full_name = "Bilal Ahmed"

# student name = "Bilal"   # Invalid

# Rule 4: Only letters, numbers and underscore
student_name_1 = "BS Information Technology"

# student-name = "BSDS"    # Invalid
# student@name = "BSDS"    # Invalid

# Rule 5: Keywords cannot be variable names
# if = 10       # Invalid
# class = "A"   # Invalid

# Rule 6: Case Sensitive
city = "Lahore"
City = "Gujranwala"

# Rule 7: Meaningful variable names
cgpa = 3.09

# Rule 8: Multiple variables in one line
course, semester, section = "Python", "8th", "A"

# Rule 9: Same value to multiple variables
x = y = z = 100

# Printing all variables
print("Name:", name)
print("Age:", _age)
print("Student Name:", full_name)
print("Department:", student_name_1)

print("city =", city)
print("City =", City)

print("CGPA =", cgpa)

print("Course =", course)
print("Semester =", semester)
print("Section =", section)

print("x =", x)
print("y =", y)
print("z =", z)