t= int(input())

l=[]
for i in range(t):
    a,b = list(map(int,input().split()[:2]))
    l.append((a,b))


for a,b in l:
    sum=0
    if b>a:
        for k in range(a+1,b):
            if k%2!=0:
                sum+=k
        print(sum)
        sum=0
    else:
        for k in range(b+1,a):
            if k%2!=0:
                sum+=k
        print(sum)
        sum=0
