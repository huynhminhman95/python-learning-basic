# Write a python program to print the contents of the directory using the os module,
# Search online for the function which does that

import os

# List contents of the current directory
entries = os.listdir()
print("Entries in current directory:")
for name in entries:
    print(name)

number = "2.5"
print(type(number))