# Crie variáveis para armazenar um nome de usuario, sua idade, se esta ativo no sistema.
# Em seguida imprima uma mensagem de boas vindas com todos os dados salvos

name = "Deblyn Prado"
age = 29
is_active = True

print("\n=====================================")
print("******* Welcome to the System *******")
print("Username: ", name)
print("Age: ", age)
if is_active:
  active_status_message = "active"
else:
  active_status_message = "inactive"
print("This user is", active_status_message, "in the system")
print("=====================================")

