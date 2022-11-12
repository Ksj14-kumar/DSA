def decreaseNumber(n):
    if(n==0):
        return 0
    print(n)
    decreaseNumber(n-1)
def increase(n):
    if(n==0):
        return 0
    increase(n-1)
    print(n)

    
# increase(5)
# decreaseNumber(5)

def IncreaseDecrease(n):
    if(n==0):
        return 0
    print(n)
    IncreaseDecrease(n-1)
    print(n)
IncreaseDecrease(5)

def factorial(n):
    if(n==1):
        return 1
    fact=n*factorial(n-1)
    return fact
print(factorial(5))
