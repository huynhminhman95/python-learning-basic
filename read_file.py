# r: read - chi cho phep doc
# w: write - ghi de du lieu
# a: append - chen them thong tin vao cuoi file
#

phone_book = open("phone_book.txt", "r")

#print(phone_book.readable()) # kiem tra xem co the doc file khong
#print(phone_book.readline()) # doc tung dong trong file
#print(phone_book.readlines()) # luu file duoi dang array
for person in phone_book.readlines():
    person = person.replace("\n", "")
    print(person)
phone_book.close()
