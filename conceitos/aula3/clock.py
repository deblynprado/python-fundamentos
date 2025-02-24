from datetime import datetime
import time

def getTime():
  current = datetime.now()
  return current.strftime("%H:%M:%S")

def getDate():
  today = datetime.today()
  return today.strftime("%Y-%m-%d")

def showClock():
  try:
    while True:
      print(f"Today is {getDate()} - The current time is: {getTime()}", end="\r")
      time.sleep(1)
  except KeyboardInterrupt:
    print("Exiting...") 
  
showClock()