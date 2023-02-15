sample = [1,2,3,4,5,6,7]

def staged_merger(liste_abr:list[int]):
    """Fusion par étages"""
    output = []
    while len(liste_abr) >= 2:
        output.append(liste_abr.pop(0) + liste_abr.pop(0))
    for i in liste_abr:
        output.append(i)
    print(output)
    return output

staged_merger(sample)