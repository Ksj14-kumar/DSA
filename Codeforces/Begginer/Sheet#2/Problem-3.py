N= int(input())

array= list(map(int,input().split()[:N]))


countEven= 0
countOdd= 0
countNegative= 0
countPositive=0

for j in array:
    if abs(j)&1==0:
        countEven+=1
    if j<0:
        countNegative+=1
    if abs(j)&1 !=0:
        countOdd+=1
    if j>0:
        countPositive+=1
    
print("Even:",countEven)
print("Odd:",countOdd)
print("Positive:",countPositive)
print("Negative:",countNegative)
