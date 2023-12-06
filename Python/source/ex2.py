num_1 = 5
num_2 = 10
lst_voti = [6,7,6,8]

if num_1 > num_2:
    print("num_1 è maggiore di num_2")
else:
    print("num_1 è minore di num_2")

numero_1 = int(input("Inserisci il primo numero "))
numero_2 = int(input("Inserisci il secondo numero "))

if numero_1 > numero_2:
    print("numero_1 è maggiore di numero_2")
else:
    print("numero_1 è minore di numero_2")

magic_number = 3

guess_number = int(input("Indivina il numoro vincente ! "))

if guess_number == magic_number:
    print("HAI VINTO")
else:
    print("Mi dispiace sei stato sfortunato")