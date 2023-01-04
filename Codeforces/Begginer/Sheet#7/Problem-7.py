N= int(input())
array= list(map(int,input().split()[:N]))

print(sum(array))
# def rec(index,a):
#     if index<=0:
#         return 0
#     return a[index-1]+rec(index-1,a)
# print(rec(len(array),array))