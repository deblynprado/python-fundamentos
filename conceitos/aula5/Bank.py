class Bank :
  def __init__(self, balance ) :
    self.__balance = balance

class Deposit(Bank) :

  def __init__(self, value) :
    self.__balance += value
    # print(f"Deposit of {value} made successfully")

account1 = Deposit(500)