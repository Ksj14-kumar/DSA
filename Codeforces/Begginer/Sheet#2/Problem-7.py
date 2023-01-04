N= int(input())
isPrime= True
for i in range(2,N):
    if N%i==0:
        isPrime= False
        break
if not isPrime:
    print("NO")
else:
    print("YES")