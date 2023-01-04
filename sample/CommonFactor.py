import math
def commonFactor(a,b):
    l=[]
    for i in range(1,min(a,b)+1):
        if a%i == b%i == 0:
            l.append(i)

    return len(l)



a=10
b=15
print(commonFactor(a,b))

print(math.log(4,2))
math.lo