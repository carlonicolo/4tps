import random

'''
Funzione che ritorna il menù di scelta noleggio auto
'''
def heading():
    print("Benvenuto nel programma di noleggio auto 4INF SRL")
    
    
def mainMenu() -> str:
    print("Inserisci: ")
    print("- (L) per il login")
    print("- (N) per registrati se sei un nuovo utente")
    print("- (X) per uscire")
    answer = input("")
    return answer
          

# LOGIN
def checkIsRegistered(name: str, password: str)-> bool:
    if (name == "Pippo" and password == "pluto"):
        return True
    else:
        return False


# Saluta utente
def greeting(name: str):
    print("Ciao ", name)
    

def mainLogin() -> str:
    print("Inserisci: ")
    print("- (N) per il noleggio di una vettura")
    print("- (R) per riconsegnare una vettura")
    print("- (X) per uscire")
    answer = input("")
    return answer


def menuOpzioniNoleggio(lst_auto: list) -> int:
    for count, value in enumerate(lst_auto):
            print(count+1, "-", value)
    option = int(input("Inserisci il numero dell'opzione scelta: "))
    return option-1
 

def importoNoleggio(marca: str, giorni_noleggio: int) -> int:
    tariffa_giornaliera = 100
    res_importo = giorni_noleggio * 100
    return res_importo


def showDatiNoleggio(lst_ricevuta: list, lst_val_noleggio: list):
    # zip the two lists together to create a list of key-value pairs
    key_value_pairs = zip(lst_ricevuta, lst_val_noleggio)
    # print(key_value_pairs)

    # convert the list of key-value pairs to a dictionary
    my_dict = dict(key_value_pairs)

    print("")
    print("### Dati noleggio ###")
    for key, value in my_dict.items() :
        print(key, "= ", value)
    
    print("#############")
    print("")
    
    
    

# Registrazione
def registraUtente() -> list:
    lst_user_data = []
    
    # input("Qual'è il tuo nome ")
    # ecc...
    return lst_user_data



# Riconsegna
def creaDatiRiconsegna() -> list:
    giorni_noleggio = random.randint(3, 9)
    print(giorni_noleggio)
    marca_auto = "Mercedes"
    importo = giorni_noleggio * 100
    # print(importo)
    lst_riconsegna_auto = [marca_auto, giorni_noleggio, importo]
    return lst_riconsegna_auto   
