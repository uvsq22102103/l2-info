fichier = input("Choisir le fichier :\n")
demande = input("Read:1/Write:2\n")
if demande == "1":
    with open(fichier,"r") as f:
        print("\nContenu de "+fichier+" :\n")
        for line in f.readlines():
            print(line)
elif demande == "2":
    with open(fichier,"a") as f:
        line = input("Saisie : ")
        while line != "":
            f.write("\n"+line)
            line = input("Saisie : ")