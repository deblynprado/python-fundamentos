# Escreva uma funcao que retorne se um numero é impar ou par

def oddNumber(number):
    if number % 2 == 0:
        return "Par"
    else:
        return "Impar"
number = input("Enter a number: ")
print(oddNumber(int(number)))