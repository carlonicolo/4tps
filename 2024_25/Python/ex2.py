# list interi
lst = [20, 30, 101, 2, 10]

# lista stringhe
lst_str = ["Ciao", "sono", "una", "lista"]

#print(len(lst))
#print(len(lst_str))

for i in range(len(lst)):
  print(lst[i])

for i in range(len(lst_str)):
  print(lst_str[i])

# TASK 1
# Verificare se il numero inserito dall'utente è
# all'interno della lista

# numero inserito dall'utente
user_number = int(input("Inserisci numero: "))

# verifica user_number se in lista
for i in range(len(lst)):
  print(lst[i])
  isEquals = (lst[i] == user_number)
  if (isEquals):
    print("Il numero ", user_number,
          " inserito dall'utente è presente nella lista")
    break

for count, value in enumerate(lst):
  #print("Valore -> ", value, " Posizione -> ", count)

  isEquals = (value == user_number)
  if (isEquals):
    print("Il numero ", value,
          " inserito dall'utente è presente nella lista alla posizione", count)
    break

# Soluzione avanzata
if (user_number in lst):
  print("ok")

print("pippo")


b = 0

# Ciclo while
while(b != 5):
  b = b + 1
  print(b)
