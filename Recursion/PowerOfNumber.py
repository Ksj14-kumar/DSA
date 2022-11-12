def power(n,k):
    if(k==0):
        return 1
    return n*power(n,k-1)

print(power(3,8))