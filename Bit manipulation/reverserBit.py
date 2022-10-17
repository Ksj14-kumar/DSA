def reverse(n):
    result=0
    for i in range(32):
        lsb= n&1
        res=lsb<<(31-i)
        result= result|res
        n= n>>1
    return result

print(reverse(36))
print(reverse(4))
print(reverse(16))