n = 100
output = []
nombres = [True]*(n+1)
for i in range(2,n+1):
    if nombres[i] is True:
        for j in range(i+1,n+1):
            if j % i == 0:
                nombres[j] = False
        output.append(i)
print(output)