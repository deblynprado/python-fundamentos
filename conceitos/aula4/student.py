class Students :
  def __init__(self, name, score) :
    self.name = name
    self.score = score
    
  def finalResult(self) :
    if self.score >= 6 :
      print(f"{self.name} passed the exam")
    else :
      print(f"{self.name} failed the exam")
      
studentName = input("Enter the student's name: ")
studentScore = input("Enter the student's score: ")

aluno = Students(studentName, float(studentScore))
aluno.finalResult()
  