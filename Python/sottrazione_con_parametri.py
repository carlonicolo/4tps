def sottrazione(a, b):
    res = a - b
    return res

num1 = 0
num2 = 0
risultato = 0

num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))
risultato = sottrazione(num1, num2)
print("Il risultato è: " + str(risultato))