# Phep toan so hoc 

import numpy as np

arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])

# phep cong - plus
result = arr_1 + arr_2

# phep tru - minus
result = arr_1 - arr_2

# phep nhan - times
result = arr_1 * arr_2

# phep chia - divide
result = arr_1 / arr_2

print(result)

# tinh tong phan tu - sum
print("Tong cac phan tu cach array.sum(): ", arr_1.sum())
print("Tong cac phan tu cach np.sum(array): ", np.sum(arr_1))


# tong tung hang va tung cot mang 2 chieu
arr_3 = np.array([
   [1,2,3],
   [4,5,6]
])

print("Tinh tong cua hang: ", arr_3.sum(axis=1))
print("Tinh tong tung cot ", arr_3.sum(axis=0))

# khi muon giu so chieu giong nhu array ban dau
row_sum = arr_3.sum(axis=1, keepdims=True)
col_sum = arr_3.sum(axis=0, keepdims=True)
print("Tinh tong cua hang giu so chieu: ", row_sum)
print("Tinh tong tung cot giu so chieu ", col_sum)

# max, min
arr_4 = np.array([1,2,3])

print("Gia tri lon nhat: ", arr_4.max())
print("Gia tri nho nhat: ", arr_4.min())
print("Gia tri trung binh nhat: ", arr_4.mean())

