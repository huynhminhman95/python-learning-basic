#NOTE: Take one more func as arguments - Nhan 1 hoac nhieu func lam doi so
# def cal_sum(nums):
#    return sum(nums)

# def higher_order_func(my_func, my_list): # my_func se chinh la tham so duoc truyen vao
#    my_sum = my_func(my_list)
#    return my_sum

# my_result = higher_order_func(cal_sum, [1,2,3])
# print("My sum: ", my_result)

#NOTE: return a func as its result - tra ve 1 func nhu ket qua tra ve
def cal_min(a, b):
   if a < b:
      return a
   else:
      return b

def cal_max(a, b):
   if a > b:
      return a
   else:
      return b

# tao higher order func va trong nay tra ve ham thong thuong
def higher_order_func(cal_name):
   if cal_name == 'min':
      return cal_min
   else:
      return cal_max

#NOTE: tinh min cua 2 so
my_result = higher_order_func("min")

print(my_result(3,5))

#NOTE: tinh max cua 2 so
my_result = higher_order_func("max")

print(my_result(3,5))