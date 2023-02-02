import string
liste = [i for i in string.ascii_letters]+['0','1','2','3','4','5','6','7','8','9']
tmax = 10 #taille max mdp (pour éviter un plantage à cause de la complexité exponentielle)
chaine = str()

def check(chaine):
    if chaine == 'PaS5w0rd':
        print('Mot de passe trouvé :',chaine)

for l in liste: #mdp de taille 1
    chaine = l
    check(chaine)
    for l2 in liste: #mdp de taille 2
        chaine = l + l2
        check(chaine)
        for l3 in liste: #mdp de taille 3
            chaine = l + l2 + l3
            check(chaine)
            for l4 in liste:
                chaine = l + l2 + l3 + l4
                check(chaine)
                for l5 in liste: #mdp de taille 1
                    chaine = l + l2 + l3 + l4 + l5
                    check(chaine)
                    for l6 in liste: #mdp de taille 2
                        chaine = l + l2 + l3 + l4 + l5 + l6
                        check(chaine)
                        for l7 in liste: #mdp de taille 3
                            chaine = l + l2 + l3 + l4 + l5 + l6 + l7
                            check(chaine)
                            for l8 in liste:
                                chaine = l + l2 + l3 + l4 + l5 + l6 + l7 + l8
                                check(chaine)

#forme de récurrence trouvée, essai de transformation ci-dessous.