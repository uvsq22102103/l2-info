from math import pi

def racine_carre(x):
    return x**(1/2)

def doubler(x):
    return (2*x)+12

def carre(x):
    return x**2

def ajout_sqrt_pi(x):
    return x+racine_carre(pi)

def ajouter_75(x):
    return x+75

def pipeline(x):
    return round(ajouter_75(ajout_sqrt_pi(carre(doubler(racine_carre(x))))),2)

print(pipeline(0))