N= int(input())


def isPrime(n):
    isTrue= True
    for i in range(2,n):
        if n%i==0:
            isTrue= False
            break
    if isTrue:
        return True
    else:
        return False




for i in range(2,N+1):
    if isPrime(i):
        print(i,end=" ")
