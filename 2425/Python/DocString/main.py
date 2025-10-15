# funzione con parametri che restituisce un intero
def somma(num1: int, num2: int) -> int:
    '''
    Calcola la somma di due numeri passati come parametri.
    
    Args:
        num1 (int): numero intero
        num2 (int): numero intero
    
    Returns:
        res (int): risultato della somma
    
    Raises:
        ValueError: Se la lista è vuota
        TypeError: Se la lista contiene elementi non numerici
    
    Example:
        >>> somma(5,6)
        11
    '''
    res = num1 + num2
    return res 


# Funzione void - non restituisce nulla
def showSomma(num1: int, num2: int):
    res = num1 + num2
    print("Funzione void")
    print("La somma è: ", res)


num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

res_somma = somma(num1, num2)
print("Il risultato della somma è: ", res_somma)
print("")
showSomma(num1,num2)

print(somma.__doc__)
