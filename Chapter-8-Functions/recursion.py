
# A recursive function must have:
# 1. Base Case      -> Stops the recursion
# 2. Recursive Case -> Calls itself again

# Example 1
# Countdown

def countdown(n):

    if n == 0:
        print("Done!")
        return

    print(n)

    countdown(n - 1)

countdown(5)

# Example 2
# Count Up

def countup(n):

    if n == 0:
        return

    countup(n - 1)

    print(n)

countup(5)

# Example 3
# Print a Name Multiple Times

def print_name(name, times):

    if times == 0:
        return

    print(name)

    print_name(name, times - 1)

print_name("Bilal", 3)

# Example 4
# Sum of Natural Numbers

def sum_numbers(n):

    if n == 1:
        return 1

    return n + sum_numbers(n - 1)

print(sum_numbers(5))

# Example 5
# Factorial

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

# Example 6
# Power of a Number

def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

print(power(2, 3))

# Example 7
# Print Characters of a String

def print_characters(text, index=0):

    if index == len(text):
        return

    print(text[index])

    print_characters(text, index + 1)

print_characters("Python")

# Important Note

# Every recursive function must have a
# Base Case.

# Wrong Example:

# def hello():
#     print("Hello")
#     hello()

# hello()
# This creates infinite recursion and
# causes a RecursionError.