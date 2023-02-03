S1 = "Java, C, et Python"
S2 = [2,3,5,7,11,13]
S3 = (1,'deux',3,True)
C = S1[:]
L = S2[:]
T = S3[:]
print(C[1:4])
print(L[2:4])
print(T[1:3])
Str = "abracadabra"
Ens = set(Str)
print(len(Str)==len(Ens))
Ens.add('e')
Ens.update([1,2,3,4,5])
E1 = {'a','b','c'}
E2 = {'c','d','e'}
print(E1.difference(E2)) # ou E1 - E2 , attention E1-E2 != E2-E1
print(E1.union(E2)) # ou E1 | E2
print(E1.intersection(E2)) # ou E1 & E2