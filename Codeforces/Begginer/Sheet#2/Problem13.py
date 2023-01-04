
a,b= list(map(int, input().split()))

l= [4,7,47,744,]
hasValue=False
for i in range(a,b):
    if i in l:
        hasValue = True
        print(i, end=" ")

if not hasValue:
    print(-1)


    