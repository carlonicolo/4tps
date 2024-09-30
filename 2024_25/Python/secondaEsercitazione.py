'''
Indovina la parola magica
Hai tre tentativi per indovinare una
parola magica 
'''
magic_word = "hello"

numero_tentativi = 0

while(numero_tentativi < 3):
    print("Inserisci la parola magica")
    try_word = input()
    if (magic_word == try_word):
        print("Hai vinto in", int(numero_tentativi + 1) ,"tentativi")
        break
    else:
        print("ritenta")
        numero_tentativi = numero_tentativi + 1

print("Primo quadro superato")
print("Hai ancora ", int(3 - numero_tentativi), " vite")


'''
for i in range(3):
    print("Inserisci la parola magica")
    try_word = input()
    if (magic_word == try_word):
        print("Hai vinto in", i+1 ," tentativi")
        break
    else:
        print("ritenta")
'''