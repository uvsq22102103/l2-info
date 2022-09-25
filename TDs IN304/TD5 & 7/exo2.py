import os


def lecture_fichier(chemin):
    fichier = open(chemin,"r")
    dico = {"étudiants":[]}
    for line in fichier.readlines():
        line = line.split()
        dico["étudiants"].append(line.pop(0))
        for i in range(len(line)):
            if len(dico.keys()) <= len(line): #création des matières
                dico["matière"+str(i+1)] = [float(line[i])]
            else: #matières déjà créees
                dico["matière"+str(i+1)].append(float(line[i]))
    print(dico)
    return(dico)


def Rajout_Max(dico:dict):
    output = ""
    for key in dico.keys():
        if key != "étudiants":
            output += dico["étudiants"][dico[key].index(max(dico[key]))] + " "
    print("Etudiants ayants eu les notes maximales dans chaques matières : " + output)
    #fichier = open("notes.txt","a")
    #fichier.write("\n"+output)
    #fichier.close()


def Rajout_Min(dico:dict):
    output = ""
    for key in dico.keys():
        if key != "étudiants":
            output += dico["étudiants"][dico[key].index(min(dico[key]))] + " "
    print("Etudiants ayants eu les notes minimales dans chaques matières : " + output)
    #fichier = open("notes.txt","a")
    #fichier.write("\n"+output)
    #fichier.close()


def Rajout_Majorant(dico:dict):
    totaux = [float() for i in range(len(dico["étudiants"]))]
    for i in range(len(dico.keys())-1):
        for j in range(len(dico["matière"+str(i+1)])):
            totaux[j] += dico["matière"+str(i+1)][j]
    for i in range(len(totaux)):
        totaux[i] = totaux[i]/(len(dico.keys())-1)
    majorant = dico["étudiants"][totaux.index(max(totaux))]
    print("Le majorant est " + majorant)
    #fichier = open("notes.txt","a")
    #fichier.write("\n"+majorant)
    #fichier.close()


def Rajout_Minorant(dico:dict):
    totaux = [float() for i in range(len(dico["étudiants"]))]
    for i in range(len(dico.keys())-1):
        for j in range(len(dico["matière"+str(i+1)])):
            totaux[j] += dico["matière"+str(i+1)][j]
    for i in range(len(totaux)):
        totaux[i] = totaux[i]/(len(dico.keys())-1)
    minorant = dico["étudiants"][totaux.index(min(totaux))]
    print("Le minorant est " + minorant)
    #fichier = open("notes.txt","a")
    #fichier.write("\n"+majorant)
    #fichier.close()


def Suppression_fichier(chemin:str):
    if os.path.exists(chemin):
        os.remove(chemin)
    else:
        print(chemin,"n'as pas été trouvé") 


dico1 = lecture_fichier("notes.txt")
Rajout_Max(dico1)
Rajout_Min(dico1)
Rajout_Majorant(dico1)
Rajout_Minorant(dico1)
#Suppression_fichier("notes.txt")