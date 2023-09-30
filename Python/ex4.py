# 27/09/2023
# Ciclo while, continue e break

print("=====BREAK=====")

# concatenazione di stringhe
#eq="="
#print(eq*10)
i = 0
while i < 6:
   i += 1
   if i == 3:
     break
   print(i)
print("==========")
print("")

print("=====CONTINUE=====")
a = 0
while a < 6:
   a += 1
   if a == 3:
     continue
   print(a)
print("==========")