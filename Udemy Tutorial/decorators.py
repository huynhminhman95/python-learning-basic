""" **** Decorators - TH khong co doi so - arguments """

# NOTE: dung higher order function thong thuong
# wrapper-ham bao va wrapped-ham duoc bao

# dung higher order function de thay doi tinh nang cua wrapped
def decorator_example(func):
   def wrapper(): # ham bao
      print("before the fucntion is called")
      func()
      print("after the function is called")
   return wrapper

# chi su dung khi ap dung decorator
@decorator_example
def say_hello(): # ham duoc bao
   print("hello")

"""
khi called say_hello() se tuong duong voi decorator_example(say_hello)
say_hello() = decorator_example(say_hello)

say_hello() = wrapper()
"""

# goi truc tiep ham duoc bao
# say_hello()

# su dung higher order function nguyen ban
# my_func = decorator_example(say_hello)
# my_func()

""" **** decorators co doi so - arguments """
# NOTE: su dung higher order function

def decorator_func(func):
   def wrapper(name, age): # ham bao
      print("Before the function is called")
      func(name, age)

   return wrapper

# ham duoc bao
@decorator_func
def say_hello_2(name, age):
   print(f"Hello {name}, you are {age} years old.")

# decorator nguyen ban
# my_func2 = decorator_func(say_hello_2)
# my_func2("Man", 30)
say_hello_2("Chi", 28)