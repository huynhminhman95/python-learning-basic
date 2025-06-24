# Ke thua trong class - inheritance
# class parent 
class Person:
   def __init__(self, name):
      self.name = name

   def print_name(self):
      print(self.name)

# class child
class Student(Person):
   # tai su dung lai ham khoi tao cua class parent
   def __init__(self, name, age):
      # self.name = name
      # super().__init__(name) # cach 1 dung super
      Person.__init__(self, name) # cach 2 dung class name
      self.age = age


my_stu = Student("Min", 10)
my_stu.print_name()
print(my_stu.age)