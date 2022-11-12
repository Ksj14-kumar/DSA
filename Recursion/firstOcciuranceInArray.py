def firstOcurrance(a,i,item):
    # top down approach
    """top-to-bottom approach"""
    if(len(a)==i):
        return -1
    if(item==a[i]):
        return i
    return firstOcurrance(a,i+1,item)
print(firstOcurrance([1,2,3,4,3,5,3,0,5],0,3))

def firstOcurranceII(a,i, item):
    """bottom-to-top approach"""
    if(len(a)==i):
        return -1
    value =firstOcurranceII(a,i+1, item)
    if(a[i]==item):
        value= i
    return value

print(firstOcurranceII([1,2,3,4,3,5,3,0,5],0,3))
