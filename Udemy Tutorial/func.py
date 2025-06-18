"""
Function in Python
"""
# def my_sum(x, y):
#     return x + y
#
# def my_print(x, y):
#     print(f"So thu nhat la {x}, So thu hai la {y}")
#
# print(my_sum(1, 2))
# my_print(1, 2)

import shutil # libraries thao tac nhu shell: cp, mv, rm, mkdir, ...
import os # cho phep tuong tac voi he thong tep-file va thu muc-folder

def copy_func(source_dir, dest_dir):
    list_name = os.listdir(source_dir)
    for file_name in list_name:
        shutil.copy(os.path.join(source_dir, file_name), os.path.join(dest_dir, file_name))

source_dir = "source_dir"
dest_dir = "dest_dir"
copy_func(source_dir, dest_dir)