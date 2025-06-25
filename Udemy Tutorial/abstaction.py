# Abstraction - tinh truu truong
# Tao he thong truu tuong trong he thong ngan hang
# yeu cau: bank want build a system gereral: moi loai tai khoan deu co the nap(deposit), rut(withdraw), tinh lai(calulate_interest)
# gia su bank co nhieu tai khoan:tiet kiem, thanh toan, bussiness
from abc import ABC, abstractmethod

class BankAccount(ABC):
   def __init__(self, balance):
      self.balance = balance

   @abstractmethod
   def withdraw(self, amount):
      pass
   
   @abstractmethod
   def deposit(self, amount):
      pass

   @abstractmethod
   def calculate_interest(self):
      pass

class SavingAccount(BankAccount):
   def withdraw(self, amount):
      if amount > self.balance:
         print('So du khong du')
      else:
         self.balance -= amount
         print(f"Da rut {amount} VND tu tai khoan tiet kiem.")
   
   def deposit(self, amount):
      self.balance += amount
      print(f"Da nap {amount} VND vao tai khoan tiet kiem.")

   def calculate_interest(self):
      interest = self.balance * 0.05
      print(f"Lai suat tai khoan tiet kiem {interest} VND")
      return interest

class CheckingAccount(BankAccount):
   def withdraw(self, amount):
      self.balance -= amount
      print(f"Da rut {amount} VND tu tai khoan thanh toan.")

   def deposit(self, amount):
      self.balance += amount
      print(f"Da nap {amount} VND vao tai khoan thanh toan.")

   def calculate_interest(self):
      print(f"Tai khoan thanh toan khong co lai suat.")
      return 0


# created object bank account
saving = SavingAccount(1000000)
checking = CheckingAccount(500000)

# saving account transfer
saving.deposit(500000)
saving.withdraw(300000)
saving.calculate_interest()

print("\n---\n")

#checking account transfer
checking.deposit(200000)
checking.withdraw(800000)
checking.calculate_interest()

