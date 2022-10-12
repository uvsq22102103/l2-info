fichier = "notes.txt"
txt = ""
with open(fichier,"r") as f:
    for line in f.readlines():
        txt += line
with open("copie"+fichier,"w") as f:
    output,i= [],0
    while len(txt) - (50*i) > 0:
        f.write(txt[i*50:(i+1)*50])
        i += 1
        print(i*50)
