# Recursion in Python

## Definition

Recursion is a programming technique in which a function calls itself.

A recursive function solves a problem by breaking it into smaller versions of the same problem.

---

## Why Use Recursion?

Recursion is useful for problems that can be divided into smaller subproblems.

Common examples:

* Factorial Calculation
* Fibonacci Series
* Tree Traversal
* Directory Navigation

---

## Basic Structure of Recursion

A recursive function has two important parts:

### 1. Base Case

The condition that stops the recursion.

### 2. Recursive Case

The part where the function calls itself.

---

## Example 1: Simple Recursion

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)

countdown(5)
```

### How It Works

```text
countdown(5)
countdown(4)
countdown(3)
countdown(2)
countdown(1)
countdown(0)
```

When `n` becomes `0`, the recursion stops.

---

## Example 2: Factorial Using Recursion

### Mathematical Formula

5! = 5 × 4 × 3 × 2 × 1

Factorial Formula:

n! = n × (n - 1)!

---

```python
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

### Step-by-Step

```text
factorial(5)
= 5 × factorial(4)

= 5 × 4 × factorial(3)

= 5 × 4 × 3 × factorial(2)

= 5 × 4 × 3 × 2 × factorial(1)

= 5 × 4 × 3 × 2 × 1

= 120
```

---

## Important Rule

Every recursive function must have a Base Case.

Wrong:

```python
def hello():
    hello()
```

This creates infinite recursion.

Result:

```text
RecursionError
```

---

## Advantages of Recursion

* Code becomes shorter.
* Useful for complex mathematical problems.
* Useful for tree and graph structures.

---

## Disadvantages of Recursion

* Uses more memory.
* Can be slower than loops.
* Infinite recursion causes errors.

---

## When to Use Recursion?

Use recursion when:

* The problem can be divided into smaller versions of itself.
* A recursive solution is easier to understand than loops.

For simple counting and repetition, loops are usually preferred.

---

## Summary

* Recursion means a function calls itself.
* Every recursive function needs a Base Case.
* Base Case stops recursion.
* Recursive Case calls the function again.
* Factorial is a common recursion example.
* Missing a Base Case causes a RecursionError.
