
industries = ["Textile", "Industrie minière", "Pétrochimie", "Construction"]
stats = [[32, 46, 24, 51], [34, 28, 46, 63], [56, 36, 32, 47], [53, 62, 39, 46]]


jeune = lambda liste: sum([1 if i<30 else 0 for i in liste])                  #
jeune_all = lambda liste: [sum([1 if i<30 else 0 for i in l]) for l in liste] #
moyenne = lambda liste: sum(liste)/len(liste)                                 #
moyenne_all = lambda liste: [sum(l)/len(l) for l in liste]                    # Copyright Aymeric

print(jeune(stats[0]))
print(jeune_all(stats))
print(moyenne(stats[0]))
print(moyenne_all(stats))

dico_ages = {secteur : (moyenne(age), jeune(age)) for secteur, age in zip(industries,stats)} # Copyright Raphaël
print(dico_ages)