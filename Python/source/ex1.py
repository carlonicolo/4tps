# Tipi di variabili
var_1 = 1               # int
var_2 = 1.0             # float
var_3 = "Ciao"          # stringa
var_4 = True            # boolean
lst_voti = [6,7,6,8]    # lista

num1 = 5
num2 = 6
somma = num1+num2
print("La somma di num1+num2 è: " + str(somma))

# Stampa tipi di variabili
print("var_1: " + str(type(var_1)))
print("var_2: " + str(type(var_2)))
print("var_3: " + str(type(var_3)))
print("somma: " + str(type(somma)))
print("lst_voti: " + str(type(lst_voti)))

# Metodi principali di una lista
print(lst_voti)
print(lst_voti[0])
print(len(lst_voti))
print(lst_voti[-1])
print(lst_voti[1:3])

greeting = "Ciao"
print("Here -> ", greeting)