N= int(input())

array= list(map(int,input().split()[:N]))


def rec(index,l):
    if index==l:
        return index
    value =rec(index+1,l)
    print(value)
    if index&1==0:
        print(array[index],end=" ")
    return value
l= len(array)
rec(0,l)
