num1 = float(input("Numero 1: "))
num2 = float(input("Numero 2: "))

operacao = ["+", "-", "*", "/"]

print("Qual operação deseja realizar?")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
op = int(input("Operação: "))

if op == 1:
  print(num1, "+", num2, "=", num1+num2)  
elif op == 2:
  print(num1, "-", num2, "=", num1-num2) 
elif op == 3:
  print(num1, "*", num2, "=", num1*num2)
elif op == 4:
  print(num1, "/", num2, "=", num1/num2)
else:
  print("Operação inválida")