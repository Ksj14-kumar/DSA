
N=int(input())
array= list(map(int,input().split()[:N]))

"Average of an array"

def total(a):
    if len(a)==0:
        return 0
    return a[0]+total(a[1:])


gt= total(array)
print(f"{gt/len(array):.6f}")
