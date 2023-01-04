
N= int(input())
def rec(n):
    if n==N+1:
        return
    print(n)
    return rec(n+1)

rec(1)  