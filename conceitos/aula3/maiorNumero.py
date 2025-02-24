# Escreva uma funcao que retorne o maior de 3 numeros

def higher_number(n1, n2, n3):
  if n1 > n2 and n1 > n3:
    print("O maior numero é: ", n1)
    return
  elif n2 > n1 and n2 > n3:
    print("O maior numero é: ", n2)
    return
  elif n3 > n1 and n3 > n2:
    print("O maior numero é: ", n3)
    return
  else:
    print("Os numeros são iguais")
    return

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
higher_number(n1, n2, n3)