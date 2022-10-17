def addBinary(a,b):
    l1,l2= len(a)-1,len(b)-1
    carry=0
    l=[]
    while l1>=0 or l2>=0:
        total=carry
        if(l1>=0):
            total +=int(a[l1])
            l1 -=1
        if(l2>=0):
            total +=int(b[l2])
            l2 -=1
        l.append(total%2)
        carry =total//2

    if (carry):
        l.append(carry)
    return "".join([f'{_}' for _ in l])[::-1]
print(addBinary("11","1"))