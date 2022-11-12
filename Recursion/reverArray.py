def reverse(a, index):
    if(index<0):
        return 

    print(a[index])
    reverse(a,index-1)

a=[1,3,4,5,6,7]
l= len(a)
print(reverse(a,l-1))

def f(a,index):
    if(index==len(a)):
        return 
    maxValue=a[index]
    if(maxValue<a[index]):
        maxValue=a[index]
    f(a,index+1)

    return maxValue

print(f(a,0))

def total(a,sum,index,path):
    if(len(a)==index):
        return 0
    # top to bottom sum
    sum[0] +=a[index]
    path.append(sum)
    # return total(a,sum,index+1,path)
    # bottom to top sum
    value =total(a,sum,index+1,path)
    return  value+a[index]
to=[0]
path= []
print(total(a,to,0,path))
print(path)
print(to)


# occurance of number
# def firstOccurance(a,index,v):
    
#     if(index ==len(a)):
#         return -1
#     if(a[index]==v):
#         return index
#     return  firstOccurance(a,index+1,v)

# print(firstOccurance([1,2,3,4,3,5,6,3,8],0,3))
def lastOccurance(a,index,v):
    
    if(index ==len(a)):
        return -1
    # if(a[len(a)-index-1]==v):
    #     return len(a)-index
    fromlast= lastOccurance(a,index+1,v)
    if(fromlast==-1):
        if(a[index]==v):
            fromlast=index
    return fromlast
print(lastOccurance([1,2,3,4,3,5,3,0,5],0,3))
def allOccurance(a,index,v,path):
    if(len(a)==index):
        return -1
    # if(a[index]==v):
    #     path.append(index)
    fromlast=allOccurance(a,index+1,v,path)
    if(a[index]==v):
        path.append(index)
    # return fromlast
path= []
a=[1,2,3,4,3,5,3,0,5]
print(allOccurance(a,0,3,path))
print(path)


key=[".;","abc","def","ghi","jkl","mno","pqrs","tu","vwx","yz"]
def getAllkeyboardCombination(s):
    if(len(s)==0):
        return [""]
    first_char= s[0] #5
    remaining_char= s[1:] #73
    remains= getAllkeyboardCombination(remaining_char)
    new= []
    for i in key[int(first_char)]:
        for j in remains:
            new.append(i+j)
    return new
print(getAllkeyboardCombination("673"))
