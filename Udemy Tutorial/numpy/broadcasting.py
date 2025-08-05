import numpy as np
"""
BROADCASTING: thuong gap khi 2 numpy array khong co cung shape-hinh dang

*** shape-hinhdang(hang, cot, dosau-deeth)

*** example 1:
arr_1 = [1,2,3]               # 1d-array; shape (3,)
arr_2 = [[4,5,6], [7,8,9]]    # 2d-array; shape (2,3)

arr_2 + arr_1
shape(2,3)       shape(3,)
4 5 6       +    1  2  3      =     5  7  9
7 8 9            1' 2' 3'           8 10 12

arr_1 thieu 1 hang. se nhan doi hang con thieu 1',2',3'. de cung so chieu
2d va cung shape -> thuc hien duoc phep tinh

*** example 2: cung chieu nhung chua cung shape

arr1 = np.array([[4,5,6], [7,8,9]])    # shape(2,3)
arr2 = np.array([[1],[2]])         # shape(2,1)

4 5 6    +     1 1' 1'    =      5  6  7
7 8 9          2 2' 2'           9 10 11

** k phai luc nao cung thuc hien duoc broadcasting

*** example 3:
shape(2,3)        shape(3,1)

4 5 6    +     1        => khong duoc
7 8 9          2
               3


"""
# arr2d = np.array([
#    [1,2,3],
#    [4,5,6]
# ])

# row_arr = arr2d.sum(axis=0, keepdims=True)
# col_arr = arr2d.sum(axis=1, keepdims=True)

# print(row_arr.shape)
# print(col_arr.shape)

# 2d array
arr1 = np.array([[4,5,6], [7,8,9]])

# 1d array
arr2 = np.array([1,2,3])

# 2d array
arr3 = np.array([[1], [2]])

# khong thuc hien duoc phep tinh
arr4 = np.array([[1],[2],[3]])

result = arr1 + arr2
result2 = arr1 + arr3
result3 = arr1 + 1
# result4 = arr1 + arr4 # khong thuc hien duoc phep tinh, do khong cung shape
print(result)
print(result2)
print(result3)
# print(result4)