class Workers :
  name = "Workers"
  salary = 0
  
  def __init__(self, name, salary) :
    self.name = name
    self.salary = salary
    
  def workerInfo(self) :
    print(f"Name: {self.name}")
    print(f"Salary: {self.salary}")
    
class Manager(Workers) :
  department = "Management"
  
  def __init__(self, name, salary, department) :
    super().__init__(name, salary)
    self.department = department
  
  def workerInfo(self):
    print(f"Name: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Department: {self.department}")
  
w1 = Workers("Mary", 3000)
w2 = Manager("Jhon", 1000, "Sales")

w1.workerInfo()

print("=====================================")

w2.workerInfo()