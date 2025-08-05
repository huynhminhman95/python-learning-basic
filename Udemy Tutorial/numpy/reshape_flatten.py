"""
   shape: hinh dang
   reshape: dinh hinh lai hinh dang
          + chuyen tu 2d array => 1d array
          + tong so luong phan tu khong thay doi
          vd: shape(2,3) => shape(6)

   Flatten: duoi ra

"""
import numpy as np

arr_1 = np.array([[1,2,3], [4,5,6]])

new_arr = np.reshape(arr_1, 6)

print(new_arr.shape)
print('--------------------------------')

new_arr_2 = arr_1.flatten()

print(new_arr_2.shape)







