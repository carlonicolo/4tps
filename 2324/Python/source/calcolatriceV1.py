# Funzioni

# Addizione
def add(num1, num2):
    risultato_add = num1 + num2
    return risultato_add

# Sottrazione


def sottr(num1, num2):
    risultato_sottr = num1 - num2
    return risultato_sottr

# Moltiplicazione


def mult(num1, num2):
    risultato_mult = num1 * num2
    return risultato_mult

# Divisione


def div(num1, num2):
    risultato_div = num1/num2
    return risultato_div


def percentuale(num1, num2):
    '''
    Prende in input due parametri, il primo è la percentuale, il secondo parametro
    è il valore del quale voglio trovare la percentuale.
    Esempio percentuale(20, 100) -> calcola il 20% di 100
    '''
    risultato = (num1*num2)/100
    return risultato


num1 = 0
num2 = 0
sceltamenu = 0
risultato = 0
risultato_real = 0.0
exit = False

while (sceltamenu != -1 or exit != True):
    # print("sceltamenu -> " + str(sceltamenu))
    # print("exit -> " + str(exit))

    '''
    print("Menu\nScegli l'operazione tra quelle disponibili inserendo il numero corrispondente\n")
    print("Inserisci i due numeri sui quali vuoi effettuare l'operazione che sceglierai dal menù")
    num1 = int(input("Inserisci il primo numero: "))
    num2 = int(input("Inserisci il secondo numero: "))
    '''
    print("\n#################################")
    print("Lista operazioni: \n 1 - Add\n 2 - Sub\n 3 - Mult\n 4 - Div\n 5 - Percentuale\n Scegli -1 per uscire\n")

    sceltamenu = int(
        input("Scegli l'operazione che vuoi effettuare sui due numeri dati: "))

    if (sceltamenu == 1):
        num1 = int(input("Inserisci il primo numero: "))
        num2 = int(input("Inserisci il secondo numero: "))
        risultato = add(num1, num2)
        exit = True
        print("Risultato addizione: " + str(risultato))

    if (sceltamenu == 2):
        num1 = int(input("Inserisci il primo numero: "))
        num2 = int(input("Inserisci il secondo numero: "))
        risultato = sottr(num1, num2)
        exit = True
        print("Risultato sottrazione: " + str(risultato))

    if (sceltamenu == 3):
        risultato = mult(num1, num2)
        exit = True
        print("Risultato moltiplicazione: " + str(risultato))

    if (sceltamenu == 4):
        num1 = int(input("Inserisci il primo numero: "))
        num2 = int(input("Inserisci il secondo numero: "))
        risultato_real = div(num1, num2)
        exit = True
        print("Risultato divisione: " + str(risultato_real))

    if (sceltamenu == 5):
        num1 = int(input("Inserisci il primo numero: "))
        num2 = int(input("Inserisci il secondo numero: "))
        risultato_real = percentuale(num1, num2)
        exit = True
        print(f"Il {num1}% di {num2} è: {risultato_real}")
        # print("Risultato percentuale: " + str(risultato_real))

    if (sceltamenu == -1):
        exit = True
        print("Bye Bye")

    print("#################################\n")

    # print("sceltamenu ***** -> " + str(sceltamenu))
    # print("exit ****** -> " + str(exit))
