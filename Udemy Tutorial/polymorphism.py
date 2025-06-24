# polymorphism - tinh da hinh

# class Cow:
#    def __init__(self, name):
#       self.name = name

#    def speak(self):
#       return self.name + " says moo"

# class Cat:
#    def __init__(self, name):
#       self.name = name

#    def speak(self):
#       return self.name + " says meomeo"

# my_cow = Cow('boo')
# my_cat = Cat('meo')

# print(my_cow.speak())
# print(my_cat.speak())

class Animal:
   def speak(self):
      return ' some sound'

class Dog (Animal):
   def speak(self):
      return 'Woof!'

my_ani = Animal()
my_dog = Dog()

print(my_ani.speak())
print(my_dog.speak())


