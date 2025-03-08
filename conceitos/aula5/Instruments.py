class Instruments : 
  def play(self) :
    print("Instrument is playing")
    
class Guitar(Instruments) :
  def play(self) :
    print("Guitar is playing")
    
class Drums(Instruments) :
  def play(self) :
    print("Drums is playing")
    
instrument = Instruments()
music = [Guitar(), Drums()]

for i in music :
  i.play()
  
instrument.play()