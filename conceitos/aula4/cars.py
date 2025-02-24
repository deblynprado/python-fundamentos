class Cars :
  def __init__(self, color, model, year) :
    self.color = color
    self.model = model
    self.year = year
  
  def showInfo(self) :
    print(f"Color: {self.color}")
    print(f"Model: {self.model}")
    print(f"Year: {self.year}")
  
  def optional(self, optional) :
    self.optional = optional
  
  def showOptionals(self) :
    print(f"Optional: {self.optional}")
  
car = Cars("Gray", "Haval H6", 2025)
car.showInfo()
print("================")

ferrari = Cars("Ferrari", "Red", 2026)
ferrari.optional("Teto Solar")
ferrari.showInfo()
ferrari.showOptionals()