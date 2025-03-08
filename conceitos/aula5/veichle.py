class Veichle :
  def move(self) :
    print("Veichle IS NOT moving")
  
class Car(Veichle) :
  def move(self) :
    print("Car IS moving")
    
car = Car()
car.move()

v = Veichle()
v.move()