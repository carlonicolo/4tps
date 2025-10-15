# Esercitazione 3

'''
Data una lista di valori restituire il numero di valori pari.

- se il numero dei valori pari è maggiore di 3 allora stampa "wow"

- altrimenti se il numero è compreso tra 0 escluso e 2 stampa "ok"

- altrimenti stampa "Oh nooo!!!"
'''

# lista numeri
lst_numbers = [1,4,7,8,10]
counter = 0
for i in range(len(lst_numbers)):
  if (lst_numbers[i] % 2 == 0):
    print("il numero", lst_numbers[i], "è pari")
    counter = counter + 1

if (counter >= 4):
  print("wow")
elif (counter == 0):
  print("oh nooooo!!!")
else:
  print("ok")