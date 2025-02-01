#**Perfil de Cliente**
#Descrição: Crie variáveis para armazenar o nome de um cliente (string), sua idade (int), seu saldo em conta (float), 
# e se ele tem cartão de crédito ativo (bool). Em seguida, imprima uma mensagem com as informações do cliente.

name = "Deblyn Prado"
age = 30
balance = 1000.00
active_card = False

if active_card:
  card_status = "active"
else:
  card_status = "inactive"

print("Customer", name, "is", age, "years old with a balance of", balance, "and", card_status, "credit card")