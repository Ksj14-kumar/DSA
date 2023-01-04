N,a,b= list(map(int,input().split()[:3]))


def total(n):
    if n==0:
        return 0
    return total(n//10)+n%10

sum=0
for i in range(1,N+1):
    res= total(i)
    if res>=a and res<=b:
        sum +=i
print(sum)