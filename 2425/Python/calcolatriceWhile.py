
'''
calcolatrice semplice con funzione raccolta dati e funzioni per le operazioni
'''

    #chiedo al utente quale operazione vuole eseguire 


# creo le funzioni che contengono le operazioni

def somma(num1,num2):
    somma_num = num1 + num2
    print("Il risultato della somma è : ", somma_num)
    return somma_num

def sottrazione (num1,num2):
    sottrazione_num = num1 - num2
    print("Il risultato della sottrazione è : ", sottrazione_num)

def moltiplicazione(num1,num2):
    if num2 != 0:
        moltiplicazione_num = num1*num2
    else:
        print("Non puoi moltiplicare per zero")

    print("Il risultato della moltiplicazione è : ", moltiplicazione_num)

def divisione (num1,num2):
    if num2 != 0:
        divisione_num = num1/num2
        print("Il risultato della divisione è : ", divisione_num)
    else:
        print("Non è possibile dividere per zero")

    


# risposta_utente = input("Quale delle seguenti operazioni desideri esegurire : ")
# risposta_utente ="no"

flag = True

while(flag):
    #creo un array che contenta le 4 operazioni e la stampi a schermo
    print("Quale delle seguenti operazioni desideri esegurire : ")
    possibili_operazioni = ["Somma","Sottrazione","Moltiplicazione","Divisione"]

    for operazione in possibili_operazioni:
        print(operazione)
    
    richiesta_utente = input("Quale operazione eseguire? ")

    print("Bene ora inserisci i numeri di tuo interesse :")
    num1 = float(input("Primo numero : "))
    num2 = float(input("Secondo numero : "))

    # richiamo le funzioni in base alla richiesta

    if richiesta_utente == "Somma":
        somma(num1,num2)
    if richiesta_utente == "Sottrazione":
        sottrazione(num1,num2)
    if richiesta_utente == "Moltiplicazione":
        moltiplicazione(num1,num2)
    if richiesta_utente == "Divisione":
        divisione(num1,num2)

    risposta_utente = input("Hai finito ? Scrivi si per uscire , no per continuare")
    if(risposta_utente == "si"):
        flag = False
    else:
        flag = True