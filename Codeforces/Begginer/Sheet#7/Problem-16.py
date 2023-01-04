N=int(input())
a= list(map(int,input().split()[:N]))


def rec(a,start,end):
    if start>end:
        return True
    if a[start]==a[end]:
        return rec(a,start+1,end-1)

    return False




res= rec(a,0,len(a)-1)
if res:
    print("YES")
else:
    print("NO")