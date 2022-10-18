fichier = "psg.txt"
content = {}
with open(fichier,"r") as f:
    txt = ""
    for line in f.readlines():
        l = line.split()
        content[l[0]] = l[1:]
nb_gens = len(content["nom"])
content["anniv"] = []
content["genre"] = []
for i in range(nb_gens):
    print(content["nom"][i],end=" ")
    print(content["prenom"][i],end=" ")
    print(content["adresse"][i],end=" ")
    print(content["codepostal"][i],end=" ")
    print(content["numtel"][i])
    content["anniv"].append(input("Votre date d'anniversaire : "))
    content["genre"].append(input("Votre genre : "))

with open(fichier,"a") as f:
    txt = "anniv " + " ".join(content["anniv"])+"\n"+"genre " + " ".join(content["genre"])
    f.write(txt)


