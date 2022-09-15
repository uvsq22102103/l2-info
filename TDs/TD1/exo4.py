mot = input("Un mot : ")
mot_r = mot[::-1]
print(mot, mot_r)
if mot == mot_r:
    print("Palindrome")

nb = int(input("Nombre : "))
nb_i = 0
while nb != nb_i:
    total = nb + nb_i
    nb, nb_i = total, int(str(total)[::-1])
print(nb, "est le palindrome résultant")
    
