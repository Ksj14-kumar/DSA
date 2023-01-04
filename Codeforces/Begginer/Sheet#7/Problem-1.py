N= int(input())


l=[]
def rec(n):
    if n==0:
        return 0
    
    return rec(n-1)

rec(N)
