from re import L


def lastOccuranceI(a,i,item):
    """ top-to-bottom approach"""
    if(len(a)==item):
        return -1
    if(a[len(a)-1-i]==item):
        return len(a)-1-i
    return lastOccuranceI(a,i+1,item)
print(lastOccuranceI([1,2,3,4,3,5,3,0,5],0,3))


def lastOccuranceII(a,i,item):
    """ bottom-to-top down apporoach"""
    if(len(a)==i):
        return -1
    value= lastOccuranceII(a,i+1,item)
    if(value==-1):
        if(a[i]==item):
            return i
    return value
print(lastOccuranceII([1,2,3,4,3,5,3,0,5],0,3))