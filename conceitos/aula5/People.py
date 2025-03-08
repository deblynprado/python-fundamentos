class Person :
  name = "Person"
  age = 0
  
  def __init__(self, name, age) :
    self.name = name
    self.age = age
    pass
  
class Student(Person) :
  register = 0
  
  def __init__(self, name, age, register) :
    super().__init__(name, age)
    self.register = register
    pass
  
student1 = Student("Mary", 20, 1234)
print(student1.name)
print(student1.age)
print(student1.register)
print("=====================================")