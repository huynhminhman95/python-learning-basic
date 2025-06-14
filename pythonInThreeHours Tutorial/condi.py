a = 400
b = 100
c = 300
x = True

print(not x)

if not a > b:
    print("a khong lon hon b")

if a > b:
    print("a lon b")
elif a < b:
    print("a be b")
else:
    print("a bang b")

if (a > b) and (a > c):
    print("a la so lon nhat")

if a == b or a == c:
    print("co it nhat 1 so bang voi gia tri cua a")