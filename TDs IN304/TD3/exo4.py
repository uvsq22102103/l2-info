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
moyennes = []
for i in dico2.keys():
    dico2[i]["mélange"] = dico2[i]["membres"] + dico2[i]["notes"] + [dico2[i]["moyenne"]]
    random.shuffle(dico2[i]["mélange"])
    moyennes.append(dico2[i]["moyenne"])

print(dico2)
best_team = dico2[moyennes.index(max(moyennes))+1]
worst_team = dico2[moyennes.index(min(moyennes))+1]
print("Meilleur groupe :",best_team["membres"],"avec",best_team["moyenne"],"de moyenne")
print("Pire groupe :",worst_team["membres"],"avec",worst_team["moyenne"],"de moyenne")