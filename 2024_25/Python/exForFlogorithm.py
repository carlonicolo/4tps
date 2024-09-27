'''
Questo programma utilizza un ciclo per esaminare un array di interi 
e dirci quanti numeri pari e quanti numeri dispari sono presenti
'''

lst = [3,4,7,8,1]
num_pari = 0
num_dispari = 0

for i in range(len(lst)):
    # print(lst[i])
    if(lst[i] % 2 == 0):
        num_pari = num_pari + 1
    else:
        num_dispari = num_dispari + 1

print("Totale numeri pari: ", num_pari)
print("Totale numeri dispari: ", num_dispari)