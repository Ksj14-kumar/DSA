from macpath import join


def power(n):
    return n&n-1==0


print(power(3))
print(power(4))
print(power(0))
