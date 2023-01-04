N= int(input())


def fact(n,dp):
    if n==0:
        return 1
    if dp[n]!=0:
        return dp[n]
    value= n*fact(n-1,dp)
    dp[n]=value
    return value

dp=[0]*(N+1)
print(fact(N,dp))
