fichier_a = "flottant.txt"
fichier_b = "arrondi.txt"

txt = ""
with open(fichier_a,"r") as f:
    for line in f.readlines():
        for mot in line.split():
            if mot != "\n":
                txt += str(int(float(mot)))+"\n"

with open(fichier_b,"w") as f:
    f.write(txt)
