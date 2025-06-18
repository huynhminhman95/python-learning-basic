"""
handling file in Python
use function open(filename, mode)
    have 4 modes
    + "r" - read file - error if the file does not exist
    + "a" - append file - creates a file if the file does not exist
    + "w" - write file - creates a file if the file does not exist
    + "x" -
"""

""" read a file """
# file_obj = open("source_dir/a.txt", "r")
# content = file_obj.read()
# print(content)
# file_obj.close()

# context manager
# with open("source_dir/a.txt", "r") as file_obj:
#     content = file_obj.read() #.readline() or .readlines()
#     print(content)

""" write a file """
# with open("source_dir/new_a.text", "w") as file_obj:
#     file_obj.write("I learning Machine Learning, Python")

""" append a file """
# with open("source_dir/a.txt", "a") as f:
#     f.write("\n I love code")

""" create a file """
with open("source_dir/new_file", "x") as f:
    pass