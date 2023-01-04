import math
N= int(input())


 
def fib(n):
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))
for i in range(N):
    print(fib(i),end=" ")

    
