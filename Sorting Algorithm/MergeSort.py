def MergeSort(a):
    if(len(a)>1):
        mid= len(a)//2

        left= a[:mid]
        right= a[mid:]
        MergeSort(left)
        MergeSort(right)
        i=j=k=0

        while i<len(left) and j<len(right):
            if(left[i]>=right[j]):
                a[k]= right[j]
                j +=1
            else:
                a[k]= left[i]
                i +=1
            k +=1
        while i<len(left):
            a[k]= left[i]
            k +=1
            i +=1
        while j<len(right):
            a[k]= right[j]
            k +=1
            j +=1
        return a
print(MergeSort([1,0,4,7,3,2]))