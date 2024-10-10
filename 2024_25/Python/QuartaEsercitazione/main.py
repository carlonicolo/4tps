import utilities as u


def main():
    try:
        lst_auto = ["BMW", "Mercedes", "Tesla", "Volvo", "Ferrari", "Maserati"]
        lst_ricevuta = ['marca','giorni', 'importo']
        lst_val_noleggio = []
        lst_dati_riconsegna = []
        
        u.heading()
        exit = False
        while(not exit):
            main_menu = u.mainMenu()
            if(main_menu == "L"):
                # login
                checkIsRegistered = u.checkIsRegistered("Pippo", "pluto")
                if(checkIsRegistered):
                    u.greeting("Pippo")
                    main_login = ""
                    while(main_login !="X"):
                        main_login = u.mainLogin()
                        if(main_login == "N"):
                            scelta_noleggio = u.menuOpzioniNoleggio(lst_auto)
                            print(lst_auto[scelta_noleggio])
                            lst_val_noleggio.append(lst_auto[scelta_noleggio])
                            lst_val_noleggio.append(4)
                            lst_val_noleggio.append(u.importoNoleggio(lst_auto[scelta_noleggio], 5))
                            # print(lst_val_noleggio)
                            u.showDatiNoleggio(lst_ricevuta, lst_val_noleggio)
                        
                            
                            
                        if(main_login == "R"):
                            # riconsegna auto
                            lst_dati_riconsegna = u.creaDatiRiconsegna()
                            print("Ok auto riconsegnata")
                            print("")
                            print("Dati riconsegna: ")
                            print("Marca: ", lst_dati_riconsegna[0])
                            print("Giorni noleggio: ", lst_dati_riconsegna[1])
                            print("Importo: ", lst_dati_riconsegna[2])
                            print("")
                            
                            
                    
            # TODO        
            if(main_menu == "N"):
                #registrazione nuovo utente
                pass
            
            if(main_menu == "X"):
                break    
        
        
    except Exception as e:
        print("Exception -> ", e) 



if __name__ == "__main__":
    main()