# **Descrição:** Solicite ao usuário que insira seu nome, sobrenome e cidade onde mora. Em seguida, exiba uma mensagem que repete as informações fornecidas.
firstName = input("Your First Name: ")
lastName = input("Your Last Name: ")
city = input("Your City: ")

print("What are your 3 favorite hobbies?")
hobby = []
hobby.append(input("Hobby 1: "))
hobby.append(input("Hobby 2: "))
hobby.append(input("Hobby 3: "))

print("What are the 3 places that you'd like to visit?")
places = []
places.append(input("Place 1: "))
places.append(input("Place 2: "))
places.append(input("Place 3: "))

print("What are your 3 favorite foods?")
foods = []
foods.append(input("Food 1: "))
foods.append(input("Food 2: "))
foods.append(input("Food 3: "))

print("Alright", firstName, lastName, "from", city, "!")
print("It looks like we have a lot of information about you.")
print("Here are your hobbies:")
count = 0
for i in hobby:
  count = count+1
  print(count, "-", i)
print()

print("Here are the places you'd like to visit:")
count = 0
for i in places:
  count = count+1
  print(count, "-", i)
print()

print("Here are your favorite foods:")
count = 0
for i in foods:
  count = count+1
  print(count, "-", i)