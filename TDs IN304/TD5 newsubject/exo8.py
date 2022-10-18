fichier_a = "test.txt"
fichier_b = "test copy.txt"

with open(fichier_a,"r") as f:
    txt_a = ""
    for line in f.readlines():
        txt_a += line

with open(fichier_b,"r") as f:
    txt_b = ""
    for line in f.readlines():
        txt_b += line

taille_a, taille_b = len(txt_a), len(txt_b)

if taille_a < taille_b: # le fichier le plus grand sera stocké en A et l'autre en B
    taille_a, taille_b = taille_b, taille_a
    fichier_a, fichier_b = fichier_b, fichier_a
    txt_a, txt_b = txt_b, txt_a

txt = ""
for i in range(taille_a):
    try:
        txt += txt_a[i] + txt_b[i]
    except:
        txt += txt_a[i]

with open("fusion.txt","w") as f:
    f.write(txt)
