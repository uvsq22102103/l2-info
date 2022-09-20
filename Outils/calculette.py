import pyperclip
nb = int(input("Nombre : "))
facteur = 3
print(facteur,"x",nb//3,"+", nb % 3)
pyperclip.copy(str(nb//3))