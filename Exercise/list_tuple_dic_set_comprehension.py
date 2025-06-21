# LIST
# Tao danh sach so chan tu 0 -> 9
list_number = []
# normally
# for i in range(10):
#    if i % 2 == 0:
#       list_number.append(i)
# comprehension 
list_number = [i*2 for i in range(10) if i % 2 == 0]
print(f"List numbers new: {list_number}")
# chuyen doi ten trong list thanh in hoa
names = ["nguyen van a", "nguyen van b", "nguyen van c"]
names_new = []
#mormally
for name in names:
   names_new.append(name.upper())
print(f"List names new: {names_new}")


# TUPLE
gen_le = (i for i in range(10) if i % 2 != 0)
print(f"Kiểu của gen_le: {type(gen_le)}")
print(f"Các phần tử của gen_le (lặp qua):")
for so in gen_le:
    print(so, end=" ")
print() # Xuống dòng
tup_le = tuple(i for i in range(10) if i % 2 != 0)
print(f"Kiểu của tup_le: {type(tup_le)}")
print(tup_le)

# DICTIONARY
numbers_dict = [1,2,3,4,5]
dict_normally = {i: i**2 for i in numbers_dict}
print(f"Dictionary normally: {dict_normally}")
# dictionary create 2 key,value
products_name = ["iphone", "samsung", "oppo"]
products_price = [1000, 2000, 3000]
products_dict = {name:price for name, price in zip(products_name, products_price)}
print(f"Dictionary products: {products_dict}")
# filter dictionary
scores_student = {'Truong': 8.5, 'Hieu': 9, 'Huy': 7, 'Huyen': 6}
students_good = {name:score for name, score in scores_student.items() if score >= 8}
print(f"Dictionary students good: {students_good}")

# SET
numbers_set = [1,2,3,4,5]
set_normally = set(numbers_set)
print(f"Set normally: {set_normally}")
# set comprehension
set_new = {i for i in numbers_set if i % 2 == 0}
print(f"Set new: {set_new}")
