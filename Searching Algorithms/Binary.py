def Binary(a, item):
    """TC= O(log(n))
    Iterative Approach
    """
    end= len(a)-1
    start= 0
    print(start+(end-start)//2)
    while end>=start:
        mid= start+(end-start)//2
        if(a[mid]==item):
            return mid
        elif (a[mid]>item):
            end= mid-1
        else:
            start = mid+1
    return -1
print(Binary([1, 2, 3, 4, 6],4))
def binary_recursive(a,item,s,e):
    """Recursive approach, TC=O(log(n))"""
    if(e>=s):
        mid= (s+e-1)//2
        if(a[mid]==item):
            return mid
        elif(a[mid]>item):
            return binary_recursive(a,item,s,mid-1)
        else:
            return binary_recursive(a,item,mid+1,e)
    else:
        return -1
a= [10, 20, 80, 30, 60, 50,110, 100, 130, 170]
s= 0
e= len(a)
print(binary_recursive(a,170,s,e))



def missing(a,n):
    
    # TODO: Missing number using Bit manipulation
    """T=O(log(n))"""
    # xor= 0
    # for i in a:
    #     xor ^=i
    # for j in range(n+1):
    #     xor ^=j
    # return xor
    # TODO: missing number using searching algorithm


print(missing([1,2,3,5],5))