# exception(ngoai le)
# la nhung loi khong mong muon xay ra trong qua trinh
# thuc thi chuong trinh
# thong thuong khi bi loi exception chuong trinh se dung dot ngot va nem ra loi
# throw an exception (Nem ra 1 ngoai le)
# Handle exception (Xu ly 1 ngoai le)

try:
    num1 = int(input("Nhap tu so: "))
    num2 = int(input("Nhap mau so: "))
    result = num1 / num2
    print(f"Thuong cua phep chia la: {result}")
except ZeroDivisionError:
    print("Mau so khong duoc be hon hoac bang 0. Vui long nhap lai")
except ValueError:
    print("Vui long nhap so nguyen duong. Vui long nhap lai")
#except:
#   print("Co loi xay ra. Lien he ky thuat vien")
