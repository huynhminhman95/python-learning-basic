#exception handling
# try:
   #run this code
# except:
   #run this code if there is an error
# else:
   #run this code if there is no error
# finally:
   #run this code no matter what
# my_dict = {"name": "John", "age": 20}
# try:
#    # result = 10/ 0
#    my_value = my_dict["name"]
# except ZeroDivisionError:
#    print("divide by zero")
# except KeyError:
#    print("key error")
# except TypeError:
#    print("error type")
# except Exception as e:
#    print(e)

try:
   num = int(input("Enter a number: "))
   print(100/num)
except ValueError:
   print("Invalid input")
except ZeroDivisionError:
   print("Cannot divide by zero")
except Exception as e:
   print(e)

print("continue")