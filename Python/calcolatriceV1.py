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


num1 = 0
num2 = 0
sceltamenu = 0
risultato = 0
risultato_real = 0.0
exit = False

while(sceltamenu != -1 or exit != True):
    #print("sceltamenu -> " + str(sceltamenu))
    #print("exit -> " + str(exit))
          
    print("Menu\nScegli l'operazione tra quelle disponibili inserendo il numero corrispondente\n")
    print("Inserisci i due numeri sui quali vuoi effettuare l'operazione che sceglierai dal menù")
    num1 = int(input("Inserisci il primo numero: "))
    num2 = int(input("Inserisci il secondo numero: "))
    
    
    print("Lista operazioni: \n 1 - Add\n 2 - Sub\n 3 - Mult\n 4 - Div\n Scegli -1 per uscire\n")
    sceltamenu = int(input("Scegli l'operazione che vuoi effettuare sui due numeri dati: "))
    if(sceltamenu == 1):
        risultato = add(num1, num2)
        exit = True
        print("Risultato " + str(risultato))
    
    if(sceltamenu == 2):
        risultato = sottr(num1, num2)
        exit = True
        print("Risultato " + str(risultato))
    
    if(sceltamenu == 3):
        risultato = mult(num1, num2)
        exit = True
        print("Risultato " + str(risultato))
    
    if(sceltamenu == 4):
        risultato_real = div(num1, num2)
        exit = True
        print("Risultato " + str(risultato_real))
    
    if(sceltamenu == -1):
        exit = True
        print("Bye Bye")
    
    #print("sceltamenu ***** -> " + str(sceltamenu))
    #print("exit ****** -> " + str(exit))
    