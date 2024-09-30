'''
Programma che valuta se un numero intero dato è 
maggiore o minore di 10.
Se è maggiore stampa i valori da 0 a 10
Se è minore stampa i valori da 10 a 0
(usando un cilco while o for)
'''

fix_number = 10
number = int(input("Inserisci un numero intero positivo: "))

if (number > fix_number):
    print("Stampo i valori da 0 a 10")
    # for i in range(start, end, increment)
    for i in range(0, fix_number+1, 1):
        print(i)
else:
    print("Stampo i valori da 0 a 10")
    for i in range(fix_number, -1, -1):
        print(i)