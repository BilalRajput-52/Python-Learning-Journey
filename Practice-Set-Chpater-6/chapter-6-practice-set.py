 
# Chapter 6 - Practice Set
 
# Question 1
# Check whether a number is positive
 

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
else:
    print("Not Positive")

# Question 2
# Check whether a person can vote

age = int(input("\nEnter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# Question 3
# Find greater number
 

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
else:
    print("Second number is greater")

# Question 4
# Grade System

marks = int(input("\nEnter marks: "))

if marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 50:
    print("Grade D")

else:
    print("Fail")

# Question 5
# Even or Odd

number = int(input("\nEnter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")