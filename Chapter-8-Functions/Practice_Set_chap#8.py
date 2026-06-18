# Chapter 8 - Functions in Python
# Practice Set
 
# Question 1
# Write a function to print "Hello, World!"

def greet():
    print("Hello, World!")

greet()
 
# Question 2
# Write a function to display a user's name.
# Take the name as input from the user.
 
def display_name(name):
    print("Welcome,", name)

user_name = input("Enter your name: ")

display_name(user_name)
 
# Question 3
# Write a function to add two numbers.
# Take numbers from the user.

def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", add(num1, num2))
 
# Question 4
# Write a function to find the average
# of two numbers.

def average(a, b):
    return (a + b) / 2

print("Average =", average(10, 20))

# Question 5
# Write a function to find the square
# of a number.

def square(number):
    return number * number

print("Square =", square(5))

# Question 6
# Write a function to find the greatest
# of three numbers.

def greatest(a, b, c):
    return max(a, b, c)

print("Greatest Number =", greatest(10, 25, 15))

# Question 7
# Write a function to convert Celsius
# into Fahrenheit.
# Formula:
# Fahrenheit = (Celsius * 9/5) + 32

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp = float(input("Enter temperature in Celsius: "))

print("Temperature in Fahrenheit =", celsius_to_fahrenheit(temp))

# Question 8
# Write a function to print the
# multiplication table of a number.

def multiplication_table(number):

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

multiplication_table(5)

# Question 9
# Write a function to check whether
# a number is even or odd.

def check_even_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"

num = int(input("Enter a number: "))

print(check_even_odd(num))

# Question 10
# Write a function to count the number
# of characters in a string.

def count_characters(text):
    return len(text)

word = input("Enter a string: ")

print("Total Characters =", count_characters(word))

# Question 11
# Write a recursive function to calculate
# the factorial of a number.

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print("Factorial =", factorial(5))

# Question 12
# Write a recursive function to calculate
# the sum of first n natural numbers.

def sum_natural_numbers(n):

    if n == 1:
        return 1

    return n + sum_natural_numbers(n - 1)

print("Sum =", sum_natural_numbers(5))

# Question 13
# Write a function that accepts a list
# and returns the largest number.

def largest_number(numbers):
    return max(numbers)

numbers = [12, 45, 67, 23, 89, 34]

print("Largest Number =", largest_number(numbers))

# Question 14
# Write a function to check whether
# a given string is a palindrome.

def is_palindrome(text):

    if text == text[::-1]:
        return True

    return False

word = input("Enter a word: ")

print(is_palindrome(word))
 
# Question 15
# Write a function to calculate the area
# of a rectangle.
# Formula:
# Area = Length × Width
 
def area_rectangle(length, width):
    return length * width

length = float(input("Enter length: "))
width = float(input("Enter width: "))

print("Area =", area_rectangle(length, width))