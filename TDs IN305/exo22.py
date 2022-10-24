def mcCarthy(n):
    if n > 100:
        return n-10
    else:
        return mcCarthy(mcCarthy(n+11))

# 1) pour n > 100 mcCarthy retourne 101-10
# 2)
print(mcCarthy(98),end=" ")
print(mcCarthy(99),end=" ")
print(mcCarthy(100))
# output ==> 91 91 91
# 3) 
for i in range(12):
    print(mcCarthy(i),end=" ")
# output ==> 91 91 91 91 91 91 91 91 91 91 91 91
# pour n <= 100 on a 101-10 = 91 comme résultat
# c'est le if n > 100: qui induit ce résultat.