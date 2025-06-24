# object : co trang thai(attribute) va hanh vi(method)
# class: template mo ta trang thai va hanh vi cua doi tuong ma class ho tro
# mot doi tuong la mot thuc the cua mot class
# NOTE: Constructor: ham khoi tao - ham goi trong qua trinh tao object của class
# ham tao co tac dung tao cac instance attribute
# NOTE: Attribute: thuoc tinh - phan chua du lieu trong class. có 2 loại:
# instance attribute va class attribute
# _Class attribute duoc tao trong than class. dai dien cho class va toan bo
# object thuoc class do
# _Instance attribute: se gan lien voi object khi duoc khoi tao(duoc khoi tao
# va gan gia tri trong ham khoi tao)
# NOTE: Method: phuong thuc - co the goi la function in class


class Person:
   # class attribute - dac trung cho toan bo class Person.count
   count = 0

   # ham khoi tao - constructor
   def __init__(self, name, age):
      self.name = name # instance attribute - gan lien voi tung doi tuong
      self.age = age
      Person.count += 1

   # define method
   def print_out(self):
      print(f"Name: {self.name} Age: {self.age}")

# create objects
person_1 = Person("Man", 30)
person_2 = Person("Chi", 27)

# print(Person.count)
# print("Name: ", person_1.name)
# person_2.print_out()

class Car:
   def __init__(self, brand, color, year):
      self.brand = brand
      self.color = color
      self.year = year
   
   def display_info(self):
      print(f"Brand: {self.brand}, Color: {self.color}, Year: {self.year}")

car_1 = Car('Toyota Camry', 'Black', 1995)
# print(car_1.display_info())

class Rectangle:
   def __init__(self, lenght, width):
      self.lenght = lenght
      self.width = width

   def area(self): # tinh dien tich
      area = self.lenght * self.width
      print(f"Dien tich: {area}")

   def perimeter(self): # tinh chu vi
      peri = 2 * (self.lenght + self.width)
      print(f"Chu vi: {peri}")

hinh_1 = Rectangle(50, 30)
# print(hinh_1.area())

class Book:
   def __init__(self, title, author, year):
      self.title = title
      self.author = author
      self.year = year
   
   def display_info(self):
      print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

list_book = [
   Book('Python', 'man', '1970'),
   Book('php', 'm22an', '1995')
]

for book in list_book:
   print(book.display_info())
