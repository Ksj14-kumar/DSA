
def sorted_array(a):
    a.sort()
    return a



def median(a1,a2):
    whole_sorted_array= sorted_array(a1+a2)
    start=0
    end= len(whole_sorted_array)-1
    mid= start+(end-start)//2
    mid_element1= whole_sorted_array[mid]
    mid_element2= whole_sorted_array[mid+1]
    return (mid_element1+mid_element2)/2
print(median([1,12,15,26,38],[2,13,17,30,45]))
