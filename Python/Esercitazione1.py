# Esercitazione N° 1 13/10/2023
# Valutare se una persona è maggiorenne o minorenne
# variabili sentinella
maggiorenne = 18
#print("Valore variabile maggiorenne: " + str(maggiorenne))

old = 60
very_old = 80
baby = 10


# variabile anni_persona
anni_persona = int(input("Quanti anni hai ? \n"))
#print("Valore anni_persona: " + str(anni_persona))

# se l'età è maggiore o uguale di 18
# stampare a video "Sei maggiorenne"
if (anni_persona >= maggiorenne):
    print("Sei maggiorenne")
else:
    print("Sei minorenne")

if (anni_persona >= very_old):
    print("Ciao nonno")
if (anni_persona >= old and anni_persona < very_old):
    print("Ciao zio")
if (anni_persona >= maggiorenne and anni_persona < old):
    print("Ciao bro")
if (anni_persona >= baby and anni_persona < maggiorenne):
    print("Ciao bocia")
if (anni_persona < baby):
    print("Ciao piccolo")



# variabile anni
magic = 20
guess = int(input("Indovina il numero vincente \n"))
contatore_tentativi = 0

while guess != magic:
    guess = int(input("Indovina il numero vincente \n"))
    contatore_tentativi += 1

if (contatore_tentativi > 5):
    print("Finalmente ce l'hai fatta ! In " + str(contatore_tentativi) + " tentativi")
else:
    print("Bravo !")    
