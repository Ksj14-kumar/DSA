N= int(input())
"3n+1 sequence"

l=[]

def rec(n):
    if n<=1:
        return 
    if n&1==0:
        n1=n//2
        l.append(n1)
        return rec(n1)
    else:
        n2= 3*n+1
        l.append(n2)
        return rec(n2)

rec(N)
l.insert(0,N)
print(len(l))