import sys

# cf exo8 pour optimisation de ce programme

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

for i in range(taille_a):
    try:
        indice = i
        if txt_a[i] != txt_b[i]:
            print(txt_a[i]+" != "+txt_b[i]+" au character n° %d" % i)
            break
    except:
        print(fichier_a+" > "+fichier_b+" pour '"+txt_a[i]+"' au character n° %d" % (i))
        sys.exit()
if taille_a < taille_b:
    print(fichier_a+" < "+fichier_b+" pour '"+txt_b[indice+1]+"' au character n° %d" % (indice+1))
    sys.exit()
print(fichier_a+" et "+fichier_b+" sont identiques en tout point.")