a,b= list(map(int,input().split()[:2]))


def rec(src,des):
    if src==des:
        return 1
    if src>des:
        return 0
    n1= rec(src+1,des)
    n2= rec(src+2,des)
    n3= rec(src+3,des)
    return n1+n2+n3

print(rec(a,b))