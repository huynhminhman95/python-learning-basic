import numpy as np

arr_1d = np.array([1,2,3])
arr_2d = np.array([[1,2], [3,4]])

# ndim - so chieu cua numpy array
print("So chieu: ", arr_1d.ndim)
print("So chieu: ", arr_2d.ndim)


# shape - the hien so phan tu trong moi chieu
print("Shape 1d array: ", arr_1d.shape)
print("Shape 2d array: ", arr_2d.shape)

# size - the hien tong so phan tu trong numpy
print("Size 1d array: ", arr_1d.size)
print("Size 2d array: ", arr_2d.size)

# dtype - ep kieu du lieu trong numpy
new_2d_arr = arr_2d.astype(np.float64)

print("New 2d array: ", new_2d_arr)