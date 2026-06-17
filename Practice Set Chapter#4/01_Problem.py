# Taking 5 items of list from user

vegetables = []

vegetables.append(input("Enter item 1: "))
vegetables.append(input("Enter item 2: "))
vegetables.append(input("Enter item 3: "))
vegetables.append(input("Enter item 4: "))
vegetables.append(input("Enter item 5: "))

print("List is:", vegetables)

# alternative method using split() items ko seperate krta ha by space 

items = input("Enter 5 items separated by space: ").split()

print("List is:", items)