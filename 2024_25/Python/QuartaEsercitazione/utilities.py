'''
Funzione che ritorna il menù di scelta noleggio auto
'''
def menu():
    print("Benvenuto nel programma di noleggio auto 4INF SRL")
    print("Elenco auto")
    

# Saluta utente
def greeting(name: str):
    print("Ciao ", name)


def menuOpzioni() -> int:
    option = int(input("Inserisci il numero dell'opzione scelta: "))
    return option


def registraUtente() -> list:
    lst_user_data = []
    
    # input("Qual'è il tuo nome ")
    # ecc...
    return lst_user_data

def checkIsRegistered(name: str, password: str)-> bool:
    if (name == "pippo" and password == "pluto"):
        return True
    else:
        return False    