fichier = "test.txt"
txt = ""
with open(fichier,"r") as f:
    for line in f.readlines():
        for chrt in line:
            if chrt == " ":
                txt += 3 * chrt
            else:
                txt += chrt
        txt += "\n"

with open(fichier,"w") as f:
    f.write(txt)