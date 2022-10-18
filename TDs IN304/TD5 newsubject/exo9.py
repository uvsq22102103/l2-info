def infos(titre:str):
    i = 1
    entree = input(titre+" n°%d : " % i)
    txt = titre +" "+ entree
    while entree != "":
        i+=1
        entree = input(titre+" n°%d : " % i)
        txt += " "+ entree
    return txt+"\n"


donnees = ["nom","prenom","adresse","codepostal","numtel"]
fichier = input("Nom du Club : ")+".txt"
with open(fichier,"w") as f:
    txt = ""
    for d in donnees:
        txt += infos(d)
    f.write(txt)