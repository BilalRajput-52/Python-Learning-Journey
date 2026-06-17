22# Topic: Nested If
 
# A Nested If means an if statement
# inside another if statement.

age = int(input("Enter your age: "))

if age >= 18:

    print("Age requirement passed")

    if age >= 21:
        print("Eligible for all activities")

    else:
        print("Eligible for limited activities")

else:
    print("Not eligible")