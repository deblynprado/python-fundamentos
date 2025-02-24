class Computers :
  def __init__(self, brand, processor, ram) :  
    self.brand = brand
    self.processor = processor
    self.ram = ram
  
dellComputer = Computers("Dell", "Intel", "16GB")
macBook = Computers("Apple", "Apple Sillicon", "8GB")

print(dellComputer.brand)
print(dellComputer.processor)
print(dellComputer.ram)
print("================")
print(macBook.brand)
print(macBook.processor)
print(macBook.ram)
print("================")