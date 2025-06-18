# Create set
# my_set = {1, 2, 3, 4, 5, 6, 7, 8,1}
# my_set = set()
# print(my_set)
# print(type(my_set))
# Khong cho phep cac phan tu lap lai
# my_set = {1, 1, 2, 3, 4, 5, 6, 7, 8}
# print(my_set)
# check set la unorder (moi lan chay lai thu tu se khac nhau)
# my_set = {'a', 'b', 'c', 'd'}
# for item in my_set:
#     print(item)
# update set (hay su dung them vao set)
# my_set = {'a', 'b', 'c', 'd'}
# my_set.add('e')
# my_set.discard('a')
# print(my_set)

# thao tac voi 2 hay nhieu sets, xem them so do Venn
my_set_1 = {'a', 'b', 'c', 'd'}
my_set_2 = {'a', 'b', 'e', 'f'}

# new_set = my_set_1.intersection(my_set_2) #giao
new_set = my_set_1.union(my_set_2) #hop
#new_set = my_set_1.symmetric_difference(my_set_2) # cac phan tu chi co moi trong moi set

print(new_set)