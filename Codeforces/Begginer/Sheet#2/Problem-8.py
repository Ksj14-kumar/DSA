N=int(input())

def rec(s):
    if s=="":
        return ""
    return rec(s[1:])+s[0]
if N==int(rec(str(N))):
    print(int(rec(str(N))))
    print("YES")
else:
    print(int(rec(str(N))))
    print("NO")
    
