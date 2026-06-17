import os

path = "C:\\Users\\bilal\\Desktop"

contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)