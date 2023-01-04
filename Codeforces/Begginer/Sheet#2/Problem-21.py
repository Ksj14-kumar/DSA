t= int(input())
l=[]
for i in range(t):
    n=int(input())
    l.append(n)

def countOnes(s,count):
    if s=="":
        return 
    if s[0]=="1":
        count[0] +=1
    return countOnes(s[1:],count)

def convert_binary_to_decimal(num,power=0):
    if num==0:
        return 0
    return (2**power)*(num%10)+convert_binary_to_decimal(num//10,power+1)

def bin_to_decimal(count):
    new_bin= int("1"*count)
    res= convert_binary_to_decimal(new_bin)
    return res


for i in l:
    binary= str(bin(i))[2:]
    count=[0]
    countOnes(binary,count)
    newNum= bin_to_decimal(count[0])
    print(newNum)





    
