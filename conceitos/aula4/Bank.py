import os

class Bank :
  def __init__(self, total = 0) :
    self.total = total
    
  def deposit(self, value) :
    os.system("clear")
    self.total += value
    print(f"Deposit of {value} made successfully")
    print(f"Your balance is {self.total}")
    self.menuOptions()
  
  def withdraw(self, value) :
    if self.total < value :
      print("Insufficient balance")
      self.menuOptions()
    else :
      self.total -= value
      print(f"Withdrawal of {value} made successfully")
      print(f"Your balance is {self.total})")
      self.menuOptions()
    
  def currentBallance(self) :
    print(f"Your current balance is {self.total}")
  
  def finalBalance(self) :
    os.system("clear")
    print(f"Your final balance is {self.total}")
  
  def menuOptions(self) :
    os.system("clear")
    print(f"Your current balce is: {account.total} \n")
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Exit")
    
    optionSelected = input("Choose an options: ")
    
    if optionSelected == "1" :
      value = float(input("Enter the amount to deposit: "))
      self.deposit(value)
    elif optionSelected == "2" :
      value = float(input("Enter the amount to withdraw: "))
      self.withdraw(value)
    elif optionSelected == "3" :
      self.finalBalance()
    else :
      print("Invalid Option. Finishing the application")
  
account = Bank()
account.menuOptions()