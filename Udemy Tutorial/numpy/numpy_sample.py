from hmac import new
import numpy as np

# tao array toan gia tri 0
zero_arr = np.zeros((3, 3))

print(zero_arr)

# create array all value 1
one_arr = np.ones((3,3))

print(one_arr)

# tao chuoi cac gia tri lien tiep nhau
new_arr = np.arange(10)

print(new_arr)

# truyen vao 3 gia tri start,stop,step(buoc nhay) - khong lay phan tu cuoi
new_arr_2 = np.arange(0, 10, 2)

print(new_arr_2)

# linspace()
new_arr_3 = np.linspace(0, 10, num=5) # bao gom phan tu dau va cuoi
# o day se tao array voi 5 so va cach deu nhau

print(new_arr_3)
