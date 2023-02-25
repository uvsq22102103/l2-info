def couples(n:int):
    return [(i,j) for i in range(1,n+1) for j in range(1,n+1)]

def coupleDiv(n:int):
    return [(i,j) for i in range(1,n+1) for j in range(1,n+1) if i % j == 0]

def coupleDiv_v2(n:int):
    r = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i % j == 0:
                r.append((i,j))
    return r

print(couples(3))
print(coupleDiv(3))
print(coupleDiv_v2(3))