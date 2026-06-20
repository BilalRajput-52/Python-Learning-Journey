# ==========================================
# Chapter 8 - Functions in Python
# Topic: Pattern Printing
# File: patterns.py
# ==========================================


# ==========================================
# 1. Square Pattern
# ==========================================

def square_pattern():

    print("Square Pattern\n")

    for row in range(5):

        for column in range(5):
            print("*", end="")

        print()

    print("\n")


# ==========================================
# 2. Right Triangle Pattern
# ==========================================

def right_triangle():

    print("Right Triangle Pattern\n")

    for row in range(1, 6):

        for column in range(row):
            print("*", end="")

        print()

    print("\n")


# ==========================================
# 3. Inverted Triangle Pattern
# ==========================================

def inverted_triangle():

    print("Inverted Triangle Pattern\n")

    for row in range(5, 0, -1):

        for column in range(row):
            print("*", end="")

        print()

    print("\n")


# ==========================================
# 4. Number Triangle Pattern
# ==========================================

def number_triangle():

    print("Number Triangle Pattern\n")

    for row in range(1, 6):

        for column in range(row):
            print(row, end=" ")

        print()

    print("\n")


# ==========================================
# 5. Increasing Number Triangle
# ==========================================

def increasing_number_triangle():

    print("Increasing Number Triangle\n")

    for row in range(1, 6):

        for column in range(1, row + 1):
            print(column, end=" ")

        print()

    print("\n")


# ==========================================
# 6. Alphabet Pattern
# ==========================================

def alphabet_pattern():

    print("Alphabet Pattern\n")

    for row in range(65, 70):

        for column in range(65, row + 1):
            print(chr(column), end=" ")

        print()

    print("\n")


# ==========================================
# 7. Pyramid Pattern
# ==========================================

def pyramid_pattern():

    print("Pyramid Pattern\n")

    rows = 5

    for row in range(rows):

        spaces = rows - row - 1
        stars = (2 * row) + 1

        print(" " * spaces + "*" * stars)

    print("\n")


# ==========================================
# 8. Reverse Pyramid Pattern
# ==========================================

def reverse_pyramid():

    print("Reverse Pyramid Pattern\n")

    rows = 5

    for row in range(rows):

        spaces = row
        stars = (2 * (rows - row)) - 1

        print(" " * spaces + "*" * stars)

    print("\n")


# ==========================================
# 9. Diamond Pattern
# ==========================================

def diamond_pattern():

    rows = 5

    # Upper Part
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

    # Lower Part
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

# diamond_pattern()


# ==========================================
# Function Calls
# ==========================================

square_pattern()

right_triangle()

inverted_triangle()

number_triangle()

increasing_number_triangle()

alphabet_pattern()

pyramid_pattern()

reverse_pyramid()

diamond_pattern()