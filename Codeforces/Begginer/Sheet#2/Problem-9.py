
array= list(map(int,input().split()))
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
print(gcd(array[0],array[1]))