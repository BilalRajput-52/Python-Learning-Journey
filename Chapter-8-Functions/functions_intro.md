# Chapter 8 - Functions in Python

## Introduction

Functions are one of the most important concepts in Python programming. As programs become larger and more complex, writing the same code repeatedly becomes inefficient. Functions help us organize code into reusable blocks, making programs easier to read, maintain, and manage.

---

## What is a Function?

### Definition

A **Function** is a reusable block of code that performs a specific task.

A function is defined once and can be called multiple times whenever needed. This helps reduce code repetition and makes programs more efficient.

---

## Without Function

When functions are not used, the same code may need to be written multiple times.

```python
print("Welcome to Python")
print("Welcome to Python")
print("Welcome to Python")
```

---

## With Function

Using a function, the code is written only once and can be reused whenever required.

```python
def welcome():
    print("Welcome to Python")

welcome()
welcome()
welcome()
```

The output remains the same, but the code becomes shorter, cleaner, and more reusable.

---

## Why Use Functions?

Functions provide several advantages:

* Code Reusability
* Better Program Organization
* Easy Maintenance
* Reduced Code Duplication
* Improved Readability
* Easier Debugging

---

## Types of Functions in Python

Python provides two main types of functions:

### 1. Built-in Functions

Built-in functions are already available in Python and can be used directly without creating them.

Examples:

```python
print()
input()
len()
type()
sum()
max()
min()
```

---

### 2. User-Defined Functions

User-defined functions are created by the programmer according to the requirements of the program.

Example:

```python
def greet():
    print("Hello Bilal")

greet()
```

---

## Function Syntax

The basic syntax of a function is:

```python
def function_name():
    # code

function_name()
```

---

## Example

```python
def greet():
    print("Welcome to Python")

greet()
```

---

## Components of a Function

Consider the following function:

```python
def greet():
    print("Hello")
```

### Breakdown

#### def

The `def` keyword is used to define a function.

#### greet

The name of the function.

#### ()

Parentheses are used to hold parameters if needed.

#### :

A colon indicates the beginning of the function body.

#### Function Body

```python
print("Hello")
```

The statements inside the function that perform the required task.

---

## Function Call

A function does not execute automatically after it is defined. It must be called explicitly.

Example:

```python
def greet():
    print("Hello")

greet()
```

Here, `greet()` is the function call that executes the function.

---

## Benefits of Functions

* Write code once and use it many times.
* Make programs easier to understand.
* Improve code structure and organization.
* Simplify testing and debugging.
* Reduce the chances of errors caused by repeated code.

---

## Chapter 8 File Structure

```text
Chapter-8-Functions
│
├── intro.py
├── function_arguments.py
├── return_statement.py
├── default_arguments.py
├── recursion.py
└── practice_set.py
```

---

## Summary

* A function is a reusable block of code.
* Functions help avoid repetition.
* Python provides built-in and user-defined functions.
* Functions are created using the `def` keyword.
* A function must be called to execute.
* Functions improve readability, organization, and maintenance of code.
