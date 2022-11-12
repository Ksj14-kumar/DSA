import math
def maxValue(a,i):
    """bottom-top-top approach"""
    if(len(a)==i):
        return -math.inf
    value= maxValue(a,i+1)
    if(value<a[i]):
        value= a[i]
    return value
a=[1,3,4,100,5,6,7]
print(maxValue(a,0))


    
