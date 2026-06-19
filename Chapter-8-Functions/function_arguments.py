
# =====================================
# FUNCTION ARGUMENTS IN PYTHON
# =====================================

# -------------------------------------
# One Argument
# -------------------------------------

def greet(name):
    print("Hello", name)

greet("Bilal")

print("\n" + "="*40 + "\n")


# -------------------------------------
# Multiple Arguments
# -------------------------------------

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Bilal", 22)

print("\n" + "="*40 + "\n")


# -------------------------------------
# Positional Arguments
# -------------------------------------

def info(name, city):
    print("Name:", name)
    print("City:", city)

info("Bilal", "Rahim Yar Khan")

print("\n" + "="*40 + "\n")


# -------------------------------------
# Keyword Arguments
# -------------------------------------

def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(age=22, name="Bilal")

print("\n" + "="*40 + "\n")


# -------------------------------------
# Default Arguments
# -------------------------------------

def greet_user(name="Guest"):
    print("Hello", name)

greet_user()
greet_user("Bilal")

print("\n" + "="*40 + "\n")


# -------------------------------------
# Arbitrary Arguments (*args)
# -------------------------------------

def numbers(*args):
    print(args)

numbers(10, 20, 30, 40)

print("\n" + "="*40 + "\n")


def add_numbers(*args):
    print("Sum =", sum(args))

add_numbers(10, 20, 30)

print("\n" + "="*40 + "\n")


# -------------------------------------
# Keyword Arbitrary Arguments (**kwargs)
# -------------------------------------

def student_details(**kwargs):
    print(kwargs)

student_details(
    name="Bilal",
    age=22,
    city="Rahim Yar Khan"
)

print("\n" + "="*40 + "\n")


def employee(**kwargs):
    print("Name:", kwargs["name"])
    print("Position:", kwargs["position"])

employee(
    name="Bilal",
    position="Data Science Intern"
)

print("\n" + "="*40 + "\n")


# -------------------------------------
# Mixing Different Types of Arguments
# -------------------------------------

def worker(name, salary=30000, *skills):
    print("Name:", name)
    print("Salary:", salary)
    print("Skills:", skills)

worker(
    "Bilal",
    50000,
    "Python",
    "Machine Learning",
    "Generative AI"
)

print("\n" + "="*40 + "\n")


# -------------------------------------
# Important Rule
# -------------------------------------

def add(a, b):
    print("Addition =", a + b)

add(10, 20)

print("\n" + "="*40 + "\n")


# -------------------------------------
# Real World Example
# -------------------------------------

def calculate_total(price, quantity):
    print("Total =", price * quantity)

calculate_total(500, 3)

print("\n" + "="*40 + "\n")


# -------------------------------------
# Order Management Example
# -------------------------------------

def order(product, quantity=1):
    print("Product:", product)
    print("Quantity:", quantity)

order("Laptop")
order("Mouse", 2)

print("\n" + "="*40 + "\n")


# -------------------------------------
# Parameter vs Argument Example
# -------------------------------------

def greet_again(name):  # name = parameter
    print("Hello", name)

greet_again("Bilal")    # Bilal = argument

