def minimum(a):
    a.sort()

    min1= a[0]
    min2=0
    for i in range(1,len(a)):
        if(min1<a[i]):
            min2=a[i]
            break

    if(min1 ==0 or min2 ==0):
        return -1
    
    return min1,min2

print(minimum([1,2,1,3,6,7]))
print(minimum([2,4,3,5,6]))
print(minimum([1,1,1,1,1,1]))