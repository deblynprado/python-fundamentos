# Crie uma funcao chamada media_lista que receba uma lista de numeros e retorne o maior entre eles

numbers = []
endCommand = "end"

userInput = print("Enter a number, or type 'end' to finish the list")

while userInput != endCommand:
    userInput = input("Enter a number: ")
    if userInput != endCommand:
        numbers.append(int(userInput))