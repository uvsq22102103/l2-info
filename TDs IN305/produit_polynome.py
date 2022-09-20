#VARIABLES##############

poly1 = [1,2,1]
poly2 = [3,1,5,1]
l_poly = []

########################
#FONCTIONS########################################

def produit_poly_entier(polynome,entier_lambda):    
    for i in range(len(polynome)):
        polynome[i] *= entier_lambda
    return(polynome)


def somme_poly(poly1,poly2):
    for i in range(len(poly2)):
        poly1[-(i+1)] += poly2[-(i+1)]
    return(poly1)

def produit_poly(polynome,entier_lambda,j):
    for i in range(len(polynome)):
        polynome[i] *= entier_lambda
    for i in range(j):
        polynome.append(0)
    return(polynome)

##################################################
#CORPS  DU PROGRAMME#######################################################

if poly1 < poly2: #Pour que poly 1 soit toujours supérieur ou égal à poly 2
    poly1,poly2 = poly2,poly1

for j in range(len(poly2)):
    l_poly.append(produit_poly(poly1.copy(),poly2[j],len(poly2)-j))
resultat = l_poly.pop(0)
for k in l_poly:
    resultat = somme_poly(resultat.copy(),k)
print("Produit polynomial : ",poly1," x ",poly2,"\nRésultat : ",resultat)