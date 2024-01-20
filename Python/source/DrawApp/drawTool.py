def drawStarsIncrement(numStars, typeOfStarts):
    """La funzione disegna un triangolo con il
    vertice in alto

    Args:
        numStars (int): numero di righe
        typeOfStarts (str): tipo di stringa da utilizzare per il disegno
    """
    for i in range(numStars):
        print("")
        for j in range(i):
            print(typeOfStarts, end="")


def drawStarsDecrement(numStars, typeOfStarts):
    """La funzione disegna un trinagolo rettangolo
    con il vertice in basso, un triangolo capovolto

    Args:
        numStars (int): numero di righe
        typeOfStarts (char): tipo di stringa da utilizzare per il disegno
    """
    for i in range(numStars, 0, -1):
        print("")
        for j in range(i):
            print(typeOfStarts, end="")


def drawPyramid(base):
    """La funzione disegna un trinagolo isoscele utilizzando
    i caratteri ASCII

    Args:
        base (int): caratteri presenti alla base del triangolo
    """
    # n = 5
    alph = 65
    for i in range(0, base):
        print(" " * (base - i), end=" ")
        for j in range(0, i + 1):
            print(chr(alph), end=" ")
            alph += 1
        # alph = 65
        print()