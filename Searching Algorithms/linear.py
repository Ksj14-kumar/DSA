
def linear(a, item):
    """TC= O(n)"""
    for i in range(len(a)):
        if(a[i] ==item):
            return i
    else:
        return -1
    

print(linear([10, 20, 80, 30, 60, 50,110, 100, 130, 170],175))
print(linear([10, 20, 80, 30, 60, 50,110, 100, 130, 170],170))