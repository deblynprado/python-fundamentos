class Secrets :
  
  def setSecret(self, secret) :
    self._secret = secret
    pass
  
  def getSecret(self) :
    return self._secret
    pass
  
secret = Secrets()
secret.setSecret("This is a secret")
print(secret.getSecret())