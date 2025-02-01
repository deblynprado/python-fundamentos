#**Cadastro de Funcionário**
#Descrição: Crie variáveis para armazenar o nome de um funcionário (string), seu número de identificação (int), 
# seu salário (float), e se ele está atualmente empregado (bool). Imprima uma mensagem contendo todas essas informações.

employee_name = "John Doe"
employee_id = 1234456
employee_salary = 3.400
is_employed = False

print("Employee Registration")
print("Name:", employee_name)
print("ID:", employee_id)
print("Salary:", employee_salary)
if is_employed:
  print("This employee is currently employed.")
else:
  print("This employee is currently unemployed.")