N= int(input())
array= list(map(int,input().split()[:N]))


maxValue= float("-inf")
def rec(index,a):
    if index==len(a):
        return float("-inf")

    value= rec(index+1,a)
    maxValue= max(value,a[index])
    return maxValue

print(rec(0,array))