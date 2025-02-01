#**Cadastro de Evento**
#Descrição: Crie variáveis para armazenar o nome de um evento (string), a data do evento (string), o número de 
# participantes esperados (int), e se o evento está com inscrições abertas (bool). Imprima uma mensagem com todas essas informações.

event_name = "Python Class"
event_date = "2025-02-01"
attendees = 100
is_open = False

print("=====", event_name, "=====")
print("Date:", event_date)
print("Expected Attendees:", attendees)
if is_open:
  print("Registrations are open!")
else:
  print("Registrations are closed now")