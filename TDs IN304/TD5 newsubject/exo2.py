fichier = "notes.txt"
txt = ""
with open(fichier,"r") as f:
    for line in f.readlines():
        txt += line if line[0] != "#" else ""
with open("copie"+fichier,"w") as f:
    f.write(txt)
