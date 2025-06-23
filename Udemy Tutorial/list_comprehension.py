"""
List comprehension cung cap cho chung ta cu phap ngan hon de tao
list moi dua tren gia tri cua list da co
"""
""" create list basic """
# list = [1,2,3,4,5]
# new_list = []
# for item in list:
#     new_list.append(item ** 2)
#
# print(new_list)

""" create list comprehension """
# list = [1,2,3,4,5]
# new_list = [x ** 2 for x in list]
# print(new_list)

""" filter element """
# new_lst = [expression for item in iterable if condition == True]
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_lst = [x for x in lst if x%2 == 1]
# print(new_lst)

""" apply function to each element """
#[expression_1 if condition == True else expression_2 for item in iterable]
# lst = [1,2,3,4,5]
# new_lst = [x+2 if x%2 == 0 else x for x in lst]
# print(new_lst)

""" Multiple loops"""
# nested_lst = [[i for i in range(5)] for _ in range(5)]
# print(nested_lst)

list_two = [[1,2,3], [4,5,6], [7,8,9]]
# flatten_lst = [num for row in list_two for num in row]
flatten_lst = []
for row in list_two:
   for col in row:
      flatten_lst.append(col)
print(f"flatten_lst: {flatten_lst}")
