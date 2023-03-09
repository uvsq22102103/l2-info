import random as rd

with open("anglaisvoc","r") as f:
    anglais = {}
    for line in f.readlines():
        i = line.index("#")
        anglais[line[0:i]] = line[i+1:]

reponses_anglais = {}
for i in range(100):
    q = rd.choice(list(anglais.keys()))
    reponses_anglais[q] = input(q+" : ")
    if reponses_anglais[q] == "":
        print("fin")
        break
    print("Pour "+q+" la réponse est "+anglais[q])
