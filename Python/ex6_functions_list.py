# 29/09/2023
# Esercizio liste e funzioni in python

'''
In questo semplice programma viene mostrato come definire
ed utilizzare una funzione in python.
Modifica di una lista aggiungendo e/o eliminando un elemento
'''

def showListContent(lst_fruits):
    print("*******************************")
    print("Contenuto del paniere")
    for x in lst_fruits:
        print(x)
    print("*******************************")

fruits = ["apple", "banana", "cherry"]
#print(type(fruits))

question = input("Hai fame ? yes/no ")
if question == "yes":
    print("Questo è quello che c'è nel frigo...")
    showListContent(fruits)
    print(" ")
    question_two = input("Ti va bene ?")
    if question_two == "yes":
        eat = input("Quale frutto vuoi mangiare ?")
        if eat in fruits:
            print("mmmm..." + eat + " ottima scelta !")
            index_eat_fruit = fruits.index(eat)
            print("Indice di eat: " + str(index_eat_fruit))
            fruits.pop(index_eat_fruit)
        else:
            print("Mi dispiace il frutto non è disponibile")
    if question_two == "no":
        add_fruit = input("Inserisci un frutto di tuo gradimento nel paniere.")
        fruits.append(add_fruit)
        print(add_fruit + " è stato aggiunto al paniere.")
    print("Ecco il contenuto del tuo paniere")
    for x in fruits:
        print(x)