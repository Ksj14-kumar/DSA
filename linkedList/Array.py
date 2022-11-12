

a=[1,2,3,4,5,6,7,8,9,10,11,12,13]
l=len(a)

#making k parts of this array element
k=3 # suppose we want to make 3 groups
while l>=k:
    # do whatever in group
    temp=k
    while temp>0:
        print("ab",l,k)
        temp -=1
    l= l-k

def nextGreaterElement(arr):
    l=[]
    for i in range(0,len(arr),1):
        value=-1
        for j in range(i+1,len(arr)):
            if(arr[i]<arr[j]):
                value= arr[j]
                break
        l.append(value)
    return l
print(nextGreaterElement([11, 13, 21, 3]))


def sublist(a1,a2):
    for i in range(len(a1)-len(a2)+1):
        if(a1[i:i+len(a2)]==a2):
            return True
    return False

a1= [1,2,3,4,5,6,7,8,10,11]
a2= [1,2]
print(sublist(a1,a2))
print(a2 in a1)
print(abs(-6))
l=[]
for i in range(len([1,2,3,4,5,6])):
    if(i&1==0):
        l.append(i)
    l.append(-i)
print(l)
