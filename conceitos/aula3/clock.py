import datetime

def getDateTime():
  current = datetime.datetime.now()
  return current.strftime("%H:%M:%S")

def showClock():
  try:
    while True:
      time = getDateTime()
      print(f"The current time is: {getDateTime()}", end="\r")
  except KeyboardInterrupt:
    print("Exiting...") 
  
showClock()