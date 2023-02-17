from itertools import islice

# alternative a enumerate : for i in range(len(seq)): seq[i], i

def indices_mots(texte:str):
    out = [0]
    for i, j in enumerate(texte,1):
        if j == " ":
            out.append(i)
    return out

def indices_mots_gen(texte:str):
    for i, j in enumerate(texte,1):
        if j == " ":
            yield i

def indices_fichier(path:str,n:int):
    with open(path,"r") as f:
        lines = "".join(f.readlines())
    return islice(indices_mots_gen(texte),n)

texte = "Four score seven years ago our fathers brought forth, upon this continent, a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal"

for i in islice(indices_mots_gen(texte),10):
    print(i,end=" ")
print()
for i in indices_fichier("test.txt",10):
    print(i, end=" ")
print()