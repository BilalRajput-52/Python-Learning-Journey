 # Function Arguments in Python

## Definition

Arguments are values passed to a function when it is called.

Arguments allow a function to work with different data each time it is executed.

---

# Parameters vs Arguments

## Parameters

Parameters are variables defined inside the function parentheses.

```python
def greet(name):
    print("Hello", name)
```

Here, `name` is a parameter.

## Arguments

Arguments are actual values passed to the function during the function call.

```python
greet("Bilal")
```

Here, `"Bilal"` is an argument.

---

# Function with One Argument

```python
def greet(name):
    print("Hello", name)

greet("Bilal")
```

Output:

```text
Hello Bilal
```

---

# Function with Multiple Arguments

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Bilal", 22)
```

Output:

```text
Name: Bilal
Age: 22
```

---

# Positional Arguments

Arguments are assigned according to their position.

```python
def info(name, city):
    print(name)
    print(city)

info("Bilal", "Rahim Yar Khan")
```

Output:

```text
Bilal
Rahim Yar Khan
```

### Important Point

Order matters in positional arguments.

```python
def student(name, age):
    print(name, age)

student(22, "Bilal")
```

Output:

```text
22 Bilal
```

The output is incorrect because the order of arguments was changed.

---

# Keyword Arguments

Keyword arguments allow us to pass values using parameter names.

In keyword arguments, the order does not matter.

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=22, name="Bilal")
```

Output:

```text
Name: Bilal
Age: 22
```

### Advantages

* Easy to read
* Order does not matter
* Reduces mistakes

---

# Default Arguments

Default arguments provide a default value to a parameter.

If no argument is passed, Python uses the default value.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Bilal")
```

Output:

```text
Hello Guest
Hello Bilal
```

### Benefits

* Makes arguments optional
* Reduces unnecessary code

---

# Arbitrary Arguments (*args)

Sometimes we do not know how many arguments will be passed to a function.

In such cases, we use `*args`.

```python
def numbers(*args):
    print(args)

numbers(10, 20, 30, 40)
```

Output:

```text
(10, 20, 30, 40)
```

### Example

```python
def add_numbers(*args):
    print(sum(args))

add_numbers(10, 20, 30)
```

Output:

```text
60
```

### Benefits

* Accepts multiple arguments
* Flexible function design

---

# Keyword Arbitrary Arguments (**kwargs)

When we want to accept multiple keyword arguments, we use `**kwargs`.

Python stores them as a dictionary.

```python
def student(**kwargs):
    print(kwargs)

student(name="Bilal", age=22, city="Rahim Yar Khan")
```

Output:

```text
{'name': 'Bilal', 'age': 22, 'city': 'Rahim Yar Khan'}
```

### Accessing Values

```python
def student(**kwargs):
    print(kwargs["name"])

student(name="Bilal", age=22)
```

Output:

```text
Bilal
```

### Benefits

* Accepts unlimited keyword arguments
* Stores data in dictionary form
* Useful for dynamic data

---

# Mixing Different Types of Arguments

A function can use multiple argument types together.

```python
def employee(name, salary=30000, *skills):
    print("Name:", name)
    print("Salary:", salary)
    print("Skills:", skills)

employee("Bilal", 50000, "Python", "Machine Learning")
```

Output:

```text
Name: Bilal
Salary: 50000
Skills: ('Python', 'Machine Learning')
```

---

# Important Rule

The number of required arguments must match the number of required parameters.

### Correct

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

### Incorrect

```python
def add(a, b):
    print(a + b)

add(10)
```

Output:

```text
TypeError: add() missing 1 required positional argument
```

---

# Real-World Example

```python
def calculate_total(price, quantity):
    print("Total =", price * quantity)

calculate_total(500, 3)
```

Output:

```text
Total = 1500
```

---

# Another Real-World Example

```python
def order(product, quantity=1):
    print("Product:", product)
    print("Quantity:", quantity)

order("Laptop")
order("Mouse", 2)
```

Output:

```text
Product: Laptop
Quantity: 1

Product: Mouse
Quantity: 2
```

---

# Summary

| Argument Type        | Description                           |
| -------------------- | ------------------------------------- |
| Positional Arguments | Values assigned according to position |
| Keyword Arguments    | Values assigned using parameter names |
| Default Arguments    | Parameters with default values        |
| *args                | Accepts multiple positional arguments |
| **kwargs             | Accepts multiple keyword arguments    |

---

# Key Points to Remember

* Parameters are variables inside the function definition.
* Arguments are values passed during the function call.
* Positional arguments depend on order.
* Keyword arguments use parameter names.
* Default arguments make parameters optional.
* *args accepts unlimited positional arguments.
* **kwargs accepts unlimited keyword arguments.
* Python allows combining different argument types in a single function.

---

### What is the difference between a Parameter and an Argument?

**Parameter:** A variable defined inside the function definition.

```python
def greet(name):
    print(name)
```

Here, `name` is a parameter.

**Argument:** A value passed to the function during the function call.

```python
greet("Bilal")
```

Here, `"Bilal"` is an argument.
