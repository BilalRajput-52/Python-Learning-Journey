# detect double space in the string

name = "Bilal      Ahmed"

print(name.find("  "))

"""
find(" ") string mein double space ko search karta hai.

Agar double space mil jaye → uska index return karta hai.
Agar double space na mile → -1 return karta hai.
"""

text = " Python   Programming   Language "

print(text.find("ing"))
print(text.find("  "))