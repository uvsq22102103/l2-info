import random as rd

notes = []

def moy_par_epreuves(nb_epreuves,nb_etudiants):
    for i in range(nb_epreuves):
        epreuvex = []
        for j in range(nb_etudiants):
            epreuvex.append(rd.randint(0,20))
        notes.append(round(sum(epreuvex)/len(epreuvex),2))
    print(notes)
    return(notes)

epreuves = 10 #int(input("Nombre d'épreuves : "))
etudiants = 100 #int(input("Nombre d'élèves : "))

moy_par_epreuves(epreuves,etudiants)