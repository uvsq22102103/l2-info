from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.simpledialog import askinteger
import matplotlib.pyplot as plt

def identite(px, py):
    compteur = 0
    i = 0
    while i < len(px):
        if px[i] == py[i]:
            compteur += 1
        i += 1
    return (compteur / len(px))*100

with open(askopenfilename(), "r") as f:
    f.readline()
    seqx = "".join(f.readlines()).replace("\n","").upper()
print("Seq x = ", seqx)

with open(askopenfilename(), "r") as f:
    f.readline()
    seqy = "".join(f.readlines()).replace("\n","").upper()

print("Seq y = ", seqy)

taille = askinteger("?Fenêtre?", "Saisissez la taille de la fenêtre désirée", initialvalue=12)
seuil = askinteger("?Seuil?", "Saisissez le seuil d'identité", initialvalue=70)

plt.title("plot TP 7")
plt.xlabel("Seq x")
plt.ylabel("Seq y")
plt.xlim(0,len(seqx))
plt.ylim(0,len(seqy))
x = 0
while x < len(seqx)-taille :
       y = 0
       while y < len(seqy)-taille :
            if identite(seqx[x:x+taille], seqy[y:y+taille]) > seuil:
                plt.scatter(x, y, c = "blue", s = 5)
            y += 1
       x += 1

plt.savefig(asksaveasfilename(defaultextension=".png", title="Enregistrez-sous"))