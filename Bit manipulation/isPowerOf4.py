def isPowerOf4(n):
    if(n<=0):
        return False
    mask = n& 0xaaaaaaaa
    notPowerOf2= (n&(n-1))
    return n and not notPowerOf2 and not mask

print(isPowerOf4(16))
print(isPowerOf4(20))