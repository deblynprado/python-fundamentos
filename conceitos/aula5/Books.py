class Books :
  title = ""
  
  def setTitle(self, title) :
    self.__title = title
    pass
  
  def getTitle(self) :
    return self.__title
    pass
  
book1 = Books()
book1.setTitle("Python Programming")
print(book1.getTitle())