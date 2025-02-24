class Person :
  def __init__(self, name) :
    self.name = name
    
    def presentation(self):
      print(f("Hello, my name is {self.name}"))