N,W= list(map(int,input().split()))

weight= []
values= []
for i in range(N):
    w,v= list(map(int,input().split()))
    weight.append(w)
    values.append(v)



def rec(weight,values,W,n):
    if W==0 or n==0:
        return 0

    if weight[n-1]<W:
        return max(values[n-1]+rec(
            weight,values,W-weight[n-1],n-1),
            rec(weight,values,W,n-1))
    elif weight[n-1]>W:
        return rec(weight,values,W,n-1)

    
print(rec(weight,values,W,len(weight)-1))
