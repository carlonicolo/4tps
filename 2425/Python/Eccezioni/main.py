import utilities as u


def main():
    try:
        # Richiamo la funzione menu() del modulo
        # utilities
        u.menu()
        
        res_option = u.menuOpzioni()
        print("Option value: ", res_option)
        
        # a = 5 / 0
        
    except Exception as e:
        print("Exception -> ", e) 



if __name__ == "__main__":
    main()