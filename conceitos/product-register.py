#**Registro de Produto**
#Descrição: Crie variáveis para armazenar o nome de um produto (string), a quantidade em estoque (int), 
# o preço por unidade (float) e se ele está disponível para venda (bool). Em seguida, imprima uma mensagem com todas essas informações.

product_name = "Coffee"
product_quantity = 10
unity_price = 5.50
is_available = True

if is_available:
  print("The product", product_name, "costs", unity_price, "and we have", product_quantity, "units in stock.")
else:
  print("The product", product_name, "is not available at the moment.")