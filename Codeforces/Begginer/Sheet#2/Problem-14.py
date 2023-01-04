S= input()
N=int(input())
l= list(map(int,input().split()[:N]))

for i in l:
    print(S*i)