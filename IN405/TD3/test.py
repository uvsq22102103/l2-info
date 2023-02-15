import os

def file_grep_string(path_in, target):
    with open(path_in,"r") as f:
        lines = f.readlines()
    n_line = 0
    r = []
    for line in lines:
        indice = 0
        while indice < len(line)-1:
            try:
                indice = line[indice:].index(target) + indice
                r.append((n_line,indice))
            except ValueError:
                break
            indice += 1
        n_line += 1
    return r

print(file_grep_string("./test.txt", "Ceci"))