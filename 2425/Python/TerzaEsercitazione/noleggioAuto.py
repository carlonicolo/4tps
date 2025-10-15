lst_auto = ["BMW", "MERCEDES"]

lst_auto_model = [["BMW",["M5","M3","M4"]],["MERCEDES",["CLASSE A","CLASSE E","AMG","GLE"]]]

print("len(lst_auto_model)")
print(len(lst_auto_model))
print(lst_auto_model)
print("")

print("len(lst_auto_model[0])")
print(len(lst_auto_model[0]))
print(lst_auto_model[0])
print("")

print("len(lst_auto_model[1])")
print(len(lst_auto_model[1]))
print(lst_auto_model[1])
print("")

for i in range(len(lst_auto_model)):
    print(lst_auto_model[i][0])


