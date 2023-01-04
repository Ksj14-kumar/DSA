t= int(input())


array=[]
for i in range(t):
    n= int(input())
    array.append(n)


def rec(i):
    if i==" ":
        return 
    rec(int(i)//10)
    print(int(i)%10,end=" ")
    # return value


for i in array:
    rec(str(i))
    print()