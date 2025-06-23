#regular expression
# a powerful tool for mathing and manipulating strings
#describes patterns in text using a sequence of characters
#searching and extracting information
#validating formats(email,phone number, etc)
#Replacing or modifying text
# bieu thuc chinh quy
# regex la mot chuoi ky tu ma co the su dung de tim kiem, thay the, hay chia nho chuoi
#Docs:https://regex101.com/

# 5 methods
#re.match() : tim kiem tu dau chuoi
#re.search() : tim kiem tu dau chuoi
#re.findall() : tim kiem tat ca chuoi
#re.split() : chia nho chuoi
#re.sub() : thay the chuoi

import re

my_string = "Hello, World! Nice to meet you"
#NOTE: re.match() : tim kiem tu dau chuoi
# match = re.match(r"Helloaaa", my_string)
# print(match)
# if match:
#     print(match.span())

#NOTE: re.search() : tim kiem tu dau chuoi
# match = re.search(r"Nice", my_string)
# print(match)
# if match:
#     print(match.span())
#NOTE: re.findall() : tim kiem tat ca chuoi
# my_string = """
#    Hello, World! Nice to meet you
#    Hello, World! Nice to meet you """
# matches = re.findall(r"Hello", my_string)
# print(matches)

#NOTE: re.split() : chia nho chuoi
# my_string = "Hello, World! Nice to meet you"
# result = re.split(r"Nice", my_string)
# print(result)

#NOTE: re.sub() : thay the chuoi
my_string = "Hello, World! Nice to meet you"
result = re.sub(r"Hello", "Hi", my_string)
print(result)