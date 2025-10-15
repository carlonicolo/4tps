# Utilizzo ciclo for

fruits = ["apple", "banana", "cherry"]
print(type(fruits))

for x in fruits:
  print(x)


for i in range(11):
  print(i)

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for i, color in enumerate(colors):
    print(i)
    ratio = ratios[i]
    print(ratio)
    #print("{}% {}".format(ratio * 100, color))


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) 
