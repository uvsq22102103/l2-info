import pickle


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


def Save_dico_pickle(dico):
    fichier = open("dico_pickle","wb")
    fichier.write(pickle.dumps(dico))
    fichier.close()


def Read_dico_pickle():
    fichier = open("dico_pickle","rb")
    dico = pickle.load(fichier)
    fichier.close()
    return(dico)


#dico1 = lecture_fichier("notes.txt")
dico1 = Read_dico_pickle()
print(dico1)