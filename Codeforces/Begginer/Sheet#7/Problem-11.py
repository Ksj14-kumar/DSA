N= int(input())

array= list(map(int,input().split()[:N]))



def rec(a,path):
    if len(a)==1:
        return a

    res=rec(a,path)
    value= res.pop()
    path.append(value)
    return res
path=[]
print(rec(array,path))