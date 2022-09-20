annee = int(input("Donnez votre date de naissance svp :  "))
l_animaux = ["singe", "coq", "chien", "porc", "rat", "boeuf", "tigre", "lapin", "dragon", "serpent", "cheval", "mouton"]
print(l_animaux[annee%12])

if (not annee % 4 and annee % 100) or not annee % 400:
    print("Année Bisextile")
else:
    print("Année non bisextile")
