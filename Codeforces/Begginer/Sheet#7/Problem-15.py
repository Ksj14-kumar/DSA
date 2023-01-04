
"Matrinx Sum"
row, col= list(map(int, input().split()[:2]))


A= []
for i in range(row):
    l= list(map(int,input().split()))
    A.append(l)



n= len(A)

B= []
for j in range(row):
    l= list(map(int,input().split()))
    B.append(l)
result= [[0]*len(A[0]) for i in range(len(A))]
for i in range(len(A)):
    for j in range(len(B[0])):
        result[i][j]= A[i][j]+B[i][j]

# print(result)

for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j],end=" ")
    print()
