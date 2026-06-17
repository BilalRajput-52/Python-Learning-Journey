# Set Methods

#  | Method           | Purpose               |
# | ---------------- | --------------------- |
# | `add()`          | Add element           |
# | `remove()`       | Remove element        |
# | `discard()`      | Remove without error  |
# | `pop()`          | Remove random element |
# | `clear()`        | Remove all elements   |
# | `union()`        | Combine sets          |
# | `intersection()` | Common elements       |


# Sample Set

numbers = {10, 20, 30, 40}

print("Original Set:")
print(numbers)

# add()
 

numbers.add(50)

print("\nAfter add():")
print(numbers)

# remove()
 
numbers.remove(20)

print("\nAfter remove():")
print(numbers)

# discard()

numbers.discard(100)

print("\nAfter discard():")
print(numbers)

# pop()
 
removed_item = numbers.pop()

print("\nRemoved Item:")
print(removed_item)

print("Updated Set:")
print(numbers)

# union()

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("\nUnion:")
print(set1.union(set2))

# intersection()
 
print("\nIntersection:")
print(set1.intersection(set2))

# clear()

set1.clear()

print("\nAfter clear():")
print(set1)