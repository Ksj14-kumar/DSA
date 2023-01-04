N= input()
def rec(n):
    if len(n)==0:
        return
    print(int(n[0]),end=" ")
    return rec(n[1:])
rec(N)