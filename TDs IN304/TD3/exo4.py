import string, random


def groupage(eleves:list,n):
    groupes = [[] for i in range(n)]
    while len(eleves) > 0:
        for i in range(n):
            if len(eleves) != 0:
                e = random.choice(eleves)
                eleves.remove(e)
                groupes[i].append(e)
    return(groupes)


nb_etudiants = 15
etudiants = list(string.ascii_lowercase[:nb_etudiants])
print(etudiants)
groupes = groupage(etudiants.copy(),5)

dico1 = {}
for i in range(len(groupes)):
    dico1[i+1] = groupes[i]
print(dico1)
dico2 = {}
for i in range(len(groupes)):
    dico2[i+1] = {"membres":groupes[i],"notes":[random.randint(0,20) for i in range(len(groupes[i]))]}
    dico2[i+1]["moyenne"] = round(sum(dico2[i+1]["notes"])/len(dico2[i+1]["notes"]),2)
print(dico2)
