# Return Statement in Python

## Definition

The `return` statement is used to send a value back from a function.

A function can perform a calculation and return the result to the place where the function was called.

---

## Why Use Return?

Without `return`, a function can only display output using `print()`.

With `return`, a function can give back a value that can be stored, reused, or used in further calculations.

---

## Function Without Return

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

In this example, the result is displayed but not returned.

---

## Function With Return

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

The function returns the result, which is stored in the variable `result`.

---

## How Return Works

```python
def square(number):
    return number * number

result = square(5)

print(result)
```

### Step-by-Step

1. Function is called with value `5`.
2. `5 * 5` is calculated.
3. The result `25` is returned.
4. The returned value is stored in `result`.
5. `result` is printed.

---

## Returning a String

```python
def greet(name):
    return "Hello " + name

message = greet("Bilal")

print(message)
```

---

## Returning Multiple Values

Python allows multiple values to be returned.

```python
def student():
    return "Bilal", 22

name, age = student()

print(name)
print(age)
```

---

## Important Rule

When a `return` statement executes, the function immediately stops.

```python
def example():

    print("First Line")

    return

    print("Second Line")
```

The second print statement will never execute.

---

## Difference Between print() and return

| print()                 | return                               |
| ----------------------- | ------------------------------------ |
| Displays output         | Sends a value back                   |
| Cannot be reused easily | Can be stored and reused             |
| Used for displaying     | Used for calculations and processing |

---

## Summary

* `return` sends a value back from a function.
* Returned values can be stored in variables.
* A function stops execution after `return`.
* Functions can return numbers, strings, lists, tuples, and other objects.
* `return` is more useful than `print()` when the result is needed later in the program.
