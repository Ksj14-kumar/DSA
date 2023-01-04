a,b= list(map(int,input().split()))
array= list(map(int,input().split()[:a]))
def rec(index,a):
    if index==len(a)-b:
        return 0
    return a[index-1]+rec(index-1,a)
print(rec(len(array),array))