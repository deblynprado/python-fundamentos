# **Descrição:** Solicite ao usuário que insira seu nome, sobrenome e cidade onde mora. Em seguida, exiba uma mensagem que repete as informações fornecidas.
firstName = input("Your First Name: ")
lastName = input("Your Last Name: ")
city = input("Your City: ")

print("What are your 3 favorite hobbies?")
hobby1 = input("Hobby 1: ")
hobby2 = input("Hobby 2: ")
hobby3 = input("Hobby 3: ")

print("What are the 3 places that you'd like to visit?")
travel1 = input("Place 1: ")
travel2 = input("Place 2: ")
travel3 = input("Place 3: ")

print("What are your 3 favorite foods?")
food1 = input("Food 1: ")
food2 = input("Food 2: ")
food3 = input("Food 3: ")

print("Alright", firstName, lastName, "from", city, "!")
print("It looks like we have a lot of information about you.\n")
print("Here are your hobbies: \n", hobby1, "\n", hobby2, "\n", hobby3)
print("Here are the places you'd like to visit: \n", travel1, "\n", travel2, "\n", travel3)
print("Here are your favorite foods: \n", food1, "\n", food2, "\n", food3)
