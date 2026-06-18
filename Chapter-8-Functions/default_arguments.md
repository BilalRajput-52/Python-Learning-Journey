# Default Arguments in Python

## Definition

Default Arguments are parameters that have a default value assigned to them.

If the user does not provide a value during the function call, Python automatically uses the default value.

---

## Why Use Default Arguments?

Default arguments make functions more flexible and easier to use.

Benefits:

* Reduce the number of required arguments.
* Prevent repetitive values from being passed again and again.
* Make functions more user-friendly.

---

## Syntax

```python
def function_name(parameter=value):
    # code
```

---

## Example 1

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Bilal")
```

### Explanation

* `greet()` uses the default value `"Guest"`.
* `greet("Bilal")` replaces the default value with `"Bilal"`.

---

## Example 2

```python
def country(name="Pakistan"):
    print("Country:", name)

country()
country("Turkey")
```

---

## Multiple Default Arguments

```python
def student(name="Bilal", age=22):
    print("Name:", name)
    print("Age:", age)

student()
```

---

## Overriding Default Values

A default value can be replaced by providing a new value during the function call.

```python
def student(name="Bilal"):
    print(name)

student("Ahmed")
```

The default value is overridden by `"Ahmed"`.

---

## Real World Example

```python
def order(item, quantity=1):
    print("Item:", item)
    print("Quantity:", quantity)

order("Laptop")
order("Mouse", 2)
```

---

## Important Rule

Parameters with default values are usually written after regular parameters.

Correct:

```python
def greet(name, message="Hello"):
    print(message, name)
```

Incorrect:

```python
def greet(message="Hello", name):
    print(message, name)
```

This will produce a SyntaxError.

---

## Summary

* Default arguments have predefined values.
* If no value is passed, the default value is used.
* Passed values override default values.
* Default arguments make functions flexible and easier to use.
