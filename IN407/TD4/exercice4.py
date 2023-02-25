BDP = [("Kanga","Elie",19,False),
       ("Aubert","Arnaud",25,True),
       ("Legrand","Pierre",54,False)]

def EnsCelibatant(BDP):
    return [(nom) for nom,_,_,mariage in BDP if not mariage]

def EnsCelibatant_v2(BDP):
    return [(nom,prenom) for nom,prenom,_,mariage in BDP if not mariage]

def EnsJeuneCelibatant(BDP):
    return [(prenom,nom) for nom,prenom,age,mariage in BDP if not mariage and age < 35]

def EnsJeuneCelibatant_v2(BDP):
    output = []
    for guest in BDP:
        if not guest[3] and guest[2] < 35:
            output.append((guest[0],guest[1]))
    return output

print(EnsCelibatant(BDP))
print(EnsJeuneCelibatant(BDP))
print(EnsJeuneCelibatant_v2(BDP))