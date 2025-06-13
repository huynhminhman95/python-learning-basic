# chi dinh 1 tu bi mat , goi y, user co the nhap nhieu lan.

secret_word = "Python"
hint = "Goi y: Day la ten mot ngon ngu lap trinh"
guess_word = ""
guess_count = 0
guess_limit = 3

print(hint)
while guess_word != secret_word:
    if guess_count < guess_limit:
        guess_word = input("Ban doan day la ngon ngu gi?")
        guess_count += 1
    else:
        break

if guess_word == secret_word:
    print("BAN DA DOAN CHINH XAC")
else:
    print("BAN DA HET LUOT DOAN ROI")