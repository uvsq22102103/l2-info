fichier = "psg.txt"
content = {}
with open(fichier,"r") as f:
    txt = ""
    for line in f.readlines():
        l = line.split()
        content[l[0]] = l[1:]
nb_gens = len(content["nom"])
print(content["codepostal"])