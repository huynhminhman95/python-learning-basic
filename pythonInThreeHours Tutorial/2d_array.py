# Mang 2 chieu, cac loop long nhau

numbers = [1,2,3]

# ma tran mang 2 chieu
# [1,2,3]
# [4,5,6]
# [7,8,9]
# tao mang 2 chieu bang cach:
# su dung mang 1 chieu lam phan tu cua mang 1 chieu khac

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for col in row:
        print(col)

