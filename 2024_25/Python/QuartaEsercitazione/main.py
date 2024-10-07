import utilities as u


def main():
    try:
        name = input("Ciao come ti chiami? ")
        u.greeting(name)
        print("Effettua il login per visualizzare il menù")
        user_name = input("Inserisci il nome utente: ")
        user_password = input("Inserisci la password")
        if(u.checkIsRegistered(user_name, user_password)):
            u.greeting(user_name)
            u.menu()
        else:
            print("Mi dispiace non hai l'autorizzazione necessaria per visualizzare il menù")
        
        
    except Exception as e:
        print("Exception -> ", e) 



if __name__ == "__main__":
    main()