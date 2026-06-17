
# Tuple Operations

# Sample Tuples

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# 1. Concatenation (+)
# Joins two tuples together.

combined = tuple1 + tuple2

print("\nConcatenation:")
print(combined)

# 2. Repetition (*)
# Repeats tuple elements.

repeated = tuple1 * 3

print("\nRepetition:")
print(repeated)

# 3. Membership (in)
# Checks whether a value exists in a tuple.

print("\nMembership Operator:")

print(20 in tuple1)
print(100 in tuple1)

 
# 4. Membership (not in)
 
print("\nNot In Operator:")

print(100 not in tuple1)
print(20 not in tuple1)
 
# 5. Length of Tuple
# Returns total number of elements.

print("\nLength:")
print(len(tuple1))

# 6. Indexing
# Accessing individual elements.

print("\nIndexing:")

print(tuple1[0])
print(tuple1[1])

# 7. Slicing
# Accessing a range of elements.

print("\nSlicing:")
print(combined[1:4])

# 8. Iteration
 
# Traversing tuple using loop.

print("\nIteration:")

for item in tuple1:
    print(item)