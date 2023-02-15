
def proportions(path:str):
    """Prend le chemin d'un fichier quelconque et retourne les
    proportions de Charactères trouvés à l'intérieur de ce fichier.\n
    str => list(n*tuple(chr,occurences))"""
    
    with open(path,"r") as f:
        texte = "".join(f.readlines()).lower()

    proportion = {}

    for i in texte:
        if i in proportion.keys():
            proportion[i] += 1
        else:
            proportion[i] = 1

    return sorted(proportion.items(), key= lambda item: item[1])
