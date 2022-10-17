txt = ""
for i in range(2,31):
    for j in range(1,21):
        txt += str(i)+" x "+str(j)+" = "+str(i*j)+"\n"
with open("table-multiplication.txt","w") as f:
    f.write(txt)