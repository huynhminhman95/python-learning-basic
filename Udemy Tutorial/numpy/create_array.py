import numpy as np

# create 1-dimensional array
arr = np.array([1,2,3.3,4,5])

# print(type(arr))
# print(arr)
# print(arr.dtype) # ep kieu du lieu

# # truy cap cac phan tu - element access
# print("Phan tu dau tien: ", arr[0])
# print(f"Phan tu cuoi cung arr[n-1]: {arr[4]} hoac arr[-1]: {arr[-1]}")
# print(arr[0:2])

# create 2-dimensional array

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr_2d[0,:])