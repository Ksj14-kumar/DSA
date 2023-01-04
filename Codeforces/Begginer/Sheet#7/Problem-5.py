S= input()

vowels= ["a","e","i","o","u"]


def rec(count,s):
    if s=="":
        return 
    if s[0].lower() in vowels:
        count[0] +=1
    rec(count,s[1:])

count= [0]
rec(count,S)
print(count[0])