# def welcome():
#   print("Welcome to the Band Name Generator.")
  
# welcome()

num1 = 3
num2 = 5

def calc(num1, num2):
  result = num1 + num2
  print(result)
  
# calc(num1, num2)

import math
def root(userNumber):
  root = math.sqrt(userNumber)
  print(root)

# userNumer = input("Enter a number: ")
# root(int(userNumer))


import os
# print(os.getcwd())

from datetime import datetime
now = datetime.now()
# print(f"The current date time is: {now.date()}")

# import sys
# import json
# pyData = json.loads({"name": "John", "age": 30, "city": "New York"})
# print(pyData)

  
# print(sys.version)

import operator
def multiply(n1, n2):
  print(f"The result of the multiplication is: {operator.mul(n1, n2)}")
  return

# number1 = float(input("Enter a number: "))
# number2 = float(input("Enter another number: "))
# multiply(number1, number2)

def greetings(name):
  user = "Visitor" if not name else name
  print(f"Hello, {user}!")
  
username = input("Enter your name: ")
greetings(username)