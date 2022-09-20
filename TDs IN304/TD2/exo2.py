import random

l = []
l_paire = []
l_impaire = []

for i in range(10):
    l.append(random.randint(10,99))
    if l[-1]%2:
        l_impaire.append(l[-1])
    else:
        l_paire.append(l[-1])

print(sum(l),round(sum(l)/len(l),2),max(l))

if random.getrandbits(1):
    l_choice = l_paire
else :
    l_choice = l_impaire
l_choice.sort()
l_choice.reverse()
del l_choice[-1], l_choice[0]
l_entiers = list(range(1,53))
coupe = random.randint(0,51)
print(coupe)
l_melange = l_entiers[coupe:52]+l_entiers[0:coupe]
print(l_melange)