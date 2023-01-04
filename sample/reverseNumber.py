def reverse(n):
    if(len(n)==0):
        return ""

    start=n[0]
    rm= n[1:]
    v=reverse(rm)
    return v+start


print(reverse("123"))

a=[ 101, 758, 315, 730,
      472, 619, 460, 479 ]
start=0
end= len(a)-1
count =0
while end>start:
    if(a[start]>a[end]):
        a[start],a[end]= a[end],a[start]
        count +=1
    end -=1
    start +=1
print(a,count)