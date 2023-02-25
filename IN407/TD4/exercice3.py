def entier(n):
    return (nbr for nbr in range(1,n+1))

def carres(n):
    return (nbr**2 for nbr in n)

def negatif(n):
    return (-nbr for nbr in n)

def carre_negatif(n):
    return (-carre for carre in (nbr**2 for nbr in (i for i in range(1,n+1))))

n = 5

print([i for i in carre_negatif(n)])

#entier(5)
#carres(5)
#negatif(5)