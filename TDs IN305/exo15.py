
def est_tas(tab,i):
    if 2*i > len(tab)-1:
        return True
    elif (2*i)+1 > len(tab)-1:
        return tab[i] > tab[2*i]
    return tab[i] > tab[2*i] and tab[i] > tab[(2*i)+1] and est_tas(tab,2*i) and est_tas(tab,(2*i)+1)

test = [0,16,10,14,11,9]

print(est_tas(test,1))
