# user enters 2 numbers
# calculate:
num1 = input("Nhap vao so 1: ")
num2 = input("Nhap vao so 2: ")

magic = ["+", "-", "*", "/"]
for mag in magic:
    result = eval(f"{num1} {mag} {num2}")
    print(f"{num1} {mag} {num2} = {result}")