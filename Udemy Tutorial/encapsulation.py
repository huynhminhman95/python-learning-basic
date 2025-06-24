# encapsulation - tinh dong goi

#NOTE: co the thay doi var trong class
# class Student:
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age

# my_student = Student("Man", 30)
# print("Truoc khi thay doi: ", my_student.name)

# my_student.name = "Minh"
# print("Sau khi thay doi: ", my_student.name)

#NOTE: them _ va __ trong bien
class Student:
   def __init__(self, name, age):
      self.__name = name
      self.age = age

my_student = Student("Man", 30)
print("Truoc khi thay doi: ", my_student._Student__name)


