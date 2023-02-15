liste_parfums = ["vanille", "chocolat", "fraise", "noix de pecan"]
valeur = 1


for i in range(len(liste_parfums)):
    print(f"la {liste_parfums[i]} est en posifion {i+1}.")
print("\n")
for i,j in enumerate(liste_parfums, valeur):
    print(f"la {j} est en position {i}.")

