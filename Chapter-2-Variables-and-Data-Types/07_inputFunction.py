# Input Function in Python

# Definition:
# The input() function is used to take input from the user during program execution.

a = input(("Enter first number :"))
b = input(("Enter  second number :"))

print ("the sum od two numbers is :", a + b)   # 4+5 is = 45 without int() 

# Important Note....>   # Without int(), Python treats input as text (string):
# Because Python joins two strings instead of adding numbers. That's why we use int() 
# for numeric input.

a = int(input(("Enter first number :")))   # with int() function
b = int(input(("Enter  second number :")))

print ("the sum od two numbers is :", a + b) 