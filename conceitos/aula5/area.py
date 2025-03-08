class Format :
  def __init__(self, value):
    self.value = value
    
  def area(self) :
    pass
    
class Circle(Format) :
  def __init__(self, value ) :
    super().__init__(value)
    
  def area(self) :
    radius = 2 * 3.14 * self.value
    print(f"Area of the circle is {radius}")
    
class Square(Format) :
  def __init__(self, value) :
    super().__init__(value)
  
  def area(self) :
    area = self.value * self.value
    print(f"Area of the square is {area}")
    
circle = Circle(4)
circle.area()

square = Square(60)
square.area()