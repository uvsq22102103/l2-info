pref = [1,2,3,4,5,6,7,8]
post = [4,3,5,2,7,8,6,1]

def IsSameTree(t_pre:list,t_pos:list):
    n1, n2 = len(t_pre),len(t_pos)
    if n1 != n2:
        return False
    elif n1 == 1:
        return True
    elif t_pre[0] != t_pos[-1]:
        return False
    
    if t_pre[1] == t_pos[-2]:
        return IsSameTree(t_pre[1:],t_pos[:-1])
    else:
        c1, c2 = t_pre.index(t_pos[-2]), t_pos.index(t_pre[1])
        return IsSameTree(t_pre[1:c1],t_pos[0:c2+1]) and IsSameTree(t_pre[c1:],t_pos[c2+1:-1])

print(IsSameTree(pref,post))