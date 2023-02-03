from string import ascii_lowercase
import matplotlib.pyplot as plt

Dico = {}
for i in ascii_lowercase:
    Dico[i] = 0
texte = "les saucisses et les saucissons secs sont dans le saloir"
for i in texte:
    if i != " ":
        Dico[i] += 1
lettres = Dico.keys()
nbr_lettres = []
for i in lettres:
    nbr_lettres.append(Dico.get(i))

plt.bar(lettres,nbr_lettres)
plt.show()