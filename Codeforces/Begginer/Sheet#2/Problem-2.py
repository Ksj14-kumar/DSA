N= int(input())


hasEven= False
for i in range(1,N+1):
    if i&1==0:
        hasEven= True
        print(i)

if not hasEven:
    print(-1)