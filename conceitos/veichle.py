#**Registro de Veículo**
#Descrição: Crie variáveis para armazenar a marca de um carro (string), o ano de fabricação (int), 
# o preço de venda (float), e se ele está disponível no estoque (bool). Em seguida, imprima uma mensagem com os detalhes do veículo.

car_brand = "BYD"
manufacturing_year = 2025
sale_price = 100000.00
is_available = True

print("Car Details")
print("Brand:", car_brand)
print("Manufacturing Year: ", manufacturing_year)
print("Sale Price: ", sale_price)
if is_available:
  print("This car is available for sale.")
else:
  print("This car is not available for sale.")