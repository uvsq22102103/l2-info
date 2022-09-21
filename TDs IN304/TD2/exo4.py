n = 100
output = []
def crible(i):
    while i <= n:
        i *= i
        try:
            nb_premier[i] = False
        except:
            pass
nb_premier = [True]*(n+1)
for i in range(2,n+1):
    if nb_premier[i] == True:
        crible(i)
        output.append(i)
print(output)