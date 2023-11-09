def somma(num1, num2):
    risultato = num1 + num2
    
    return risultato

# Main
num1 = int(input("Inserisci il primo numero: "))
print("Valore num1 " + str(num1))

num2 = int(input("inserisci il secondo numero: "))
print("Il valore di num2 è: " + str(num2))

risultato = num1 + num2
print("La somma di num1 e num2 è: " + str(risultato))

# incremento le variabili di 1
num1 = num1 + 1
num2 = num2 + 1

# invoco la funzione somma(num1, num2)
risultato = somma(num1, num2)
print("Il risultato della funzione somma è: " + str(risultato))
