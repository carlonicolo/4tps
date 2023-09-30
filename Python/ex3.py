# 26/09/2023

magic_number = 3

try_counter = 1
max_try = 3

while try_counter < 4:
    if try_counter == max_try:
        print("Ultimo tentativo")
    guess_number = int(input("Indivina il numoro vincente ! "))
    if guess_number == magic_number:
        print("HAI VINTO")
    try_counter += 1
print("GAME OVER")
