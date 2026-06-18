# Function Arguments in Python

## Definition

Arguments are values passed to a function when it is called.

Arguments allow a function to work with different data each time it is executed.

---

## Parameters vs Arguments

### Parameters

Parameters are variables defined inside the function parentheses.

```python
def greet(name):
    print("Hello", name)
```

Here, `name` is a parameter.

### Arguments

Arguments are actual values passed to the function during the function call.

```python
greet("Bilal")
```

Here, `"Bilal"` is an argument.

---

## Function with One Argument

```python
def greet(name):
    print("Hello", name)

greet("Bilal")
```

---

## Function with Multiple Arguments

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Bilal", 22)
```

---

## Positional Arguments

Arguments are assigned according to their position.

```python
def info(name, city):
    print(name)
    print(city)

info("Bilal", "Rahim Yar Khan")
```

---

## Important Rule

The number of arguments must match the number of parameters.

Correct:

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Incorrect:

```python
def add(a, b):
    print(a + b)

add(10)
```

This will produce an error because one argument is missing.

---

## Real World Example

```python
def calculate_total(price, quantity):
    print("Total =", price * quantity)

calculate_total(500, 3)
```

---

## Summary

* Parameters are variables inside the function definition.
* Arguments are actual values passed during function call.
* Functions can accept one or multiple arguments.
* Positional arguments follow the order of parameters.
* The number of arguments should match the number of parameters.
