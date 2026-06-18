# Example 1

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Bilal")

# Example 2
 
def country(name="Pakistan"):
    print("Country:", name)

country()
country("Turkey")

# Multiple Default Arguments
 
def student(name="Bilal", age=22):
    print("Name:", name)
    print("Age:", age)

student()

# Real World Example

def order(item, quantity):
    print("Item:", item)
    print("Quantity:", quantity)

order("Laptop",1)
order("Mouse", 2)