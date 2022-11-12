def reversed(a):
    # withour creating an auxiliary space
    for i in range(len(a)-1,-1,-1):
        rm= a.pop(i)
        a.insert(len(a),rm)
    return a
a=[1,2,3,4,5,6,7,8,8,9]
print(reversed(a))