N= int(input())

j1=1
j2=4
for i in range(N):
    for j in range(j1,j2):
        print(j, end=" ")
    j1=j2+1
    j2=j1+3
    print("PUM")
    
