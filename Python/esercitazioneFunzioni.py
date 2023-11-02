# Programma che da la possibiltà di sommare, dividere, sottrarre e moltiplicare due numeri.
# Devono essere implementate 4 funzioni una per ogni operazione

# Funzione somma che prende due parametri interi
def somma(a, b):
    print("Sono detro la funzione somma")
    c = a + b 
    print("La somma dei due valori a e b è: " + str(c))
    print(f'La somma è: {c}')
    print("Sto uscendo dalla funzione somma")
    return c


# Non si può divivere per 0
def divisione(a, b):
    if num2 == 0:
        print("La divisione per 0 non è possibile !!!")
        raise ValueError('some error')
    else:
        print(str(type(a)) + " " + str(type(b)))
        print(int(a)/int(b))
        return int(a)/int(b)


# Non si può divivere per 0
def moltiplicazione(a, b):
    pass


# Non si può divivere per 0
def sottrazione(a, b):
    pass


numeri = input("Inserisci due numeri nel formato (x y): ")
print(f'Variabile numeri prima dello split -> {numeri}')

numeri = numeri.split(" ")
print(f'Dopo lo split -> {numeri}') 

num1 = numeri[0]
num2 = numeri[1]

try:
    operazione = input("Quale tipo di operazione vuoi calcolare ? ")
    if operazione == "somma":
        x = somma(num1, num2)
        print("La somma è : " + str(x))
    if operazione == "moltiplicazione":
        moltiplicazione(num1, num2)
    if operazione == "sottrazione":
        sottrazione(num1, num2)
    if operazione == "divisione":
        if int(num2) == 0:
            print("Divisione non possibile")
        else:
            div = divisione(num1, num2)
            print("La divisione è uguale a: " + str(div))
except ValueError:
    pass
    
        
    

# x = somma(10,20)
# print("Valore di somma fuori dalla funzione è: " + str(x) )