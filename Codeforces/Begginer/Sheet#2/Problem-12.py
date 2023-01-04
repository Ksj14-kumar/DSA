
N= int(input())

l= []
for i in range(N):
    n= input()
    l.append(n)

def rev(j):
    if j=="":
        return 
    rev(j[1:])
    print(j[0],end=" ")

for j in l:
    rev(j)
    print()