import string, random


def ecriture_fichier(dico:dict):
    output = ""
    for i in range(len(dico["étudiants"])):
        for key in dico.keys():
            if key != "étudiants":
                output += str(dico[key][i]) + " "
            elif i == 0:
                output += dico[key][i] + " "
            else:
                output += "\n" + dico[key][i] + " "
    fichier = open("notes.txt","w")
    fichier.write(output)
    fichier.close()


etudiants = [string.ascii_lowercase[i] for i in range(5)]
notes = [[round(random.uniform(0.00,20.00),2) for i in range(5)] for i in range(4)]
dico1 = {"étudiants":etudiants}
for i in range(len(notes)):
    dico1["matière"+str(i+1)] = notes[i]
ecriture_fichier(dico1)