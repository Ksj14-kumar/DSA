t= int(input())

l=[]
for i in range(t):
    n= int(input())
    l.append(n)


def fact(n):
    # factorial using bigInt
    fact=1
    for j in range(2,n+1):
        fact*=j
    return fact

for i in l:
    print(fact(i))
