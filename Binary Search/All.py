def Binary_search_itr(a,target):
    "iterative approach"
    start= 0
    end= len(a)-1

    while end>=start:
        mid= start+(end-start)//2 # by use this instead of (end+start)//2 for avoid integer overflow

        if a[mid]==target: 
            return mid
        elif a[mid]>target: # by we not use <=, bcoz we already use ==
            start= mid+1
        elif a[mid]<target: # by we not use <=, bcoz we already use ==
            end= mid-1
    return -1


def Binary_search_rec(a,target):
    "recursive approach"
    def rec(a,start,end,target):
        if start>end:
            return
        if end>=start:
            mid=  start+(end-start)//2

            if a[mid]==target:
                return mid
            if a[mid]<target: # by we not use <=, bcoz we already use ==
                return rec(a,mid+1,end,target)
            if a[mid]>target: # by we not use <=, bcoz we already use ==
                return rec(a,start,mid-1,target)
        return -1
    start=0
    end= len(a)-1
    return rec(a,start,end,target)


def Binary_search_template(a,target):
    "use this templates for tricky handing"
    start= 0
    end= len(a)
    while end>start:
        mid= start+(end-start)//2

        if a[mid]==target:
            return mid
        elif target<a[mid]:# by we not use <=, bcoz we already use ==
            end=mid
        else:
            start=mid+1
    return start


"=====================PROBLEM START HERE LeetCode and more==============================="












"===================Solved Problem by template Binary Search=============="

def search_in_rooted_sorted_array_no_duplicates_33(a,target):
    # [4,5,6,7,0,1,2]
    start= 0
    end= len(a)-1
    while end>=start:
        mid= start+(end-start)//2
        if a[mid]==target:
            return mid
        if a[mid]>=a[start]: # left array is sorted
            if target>=a[start] and target<a[mid]:
                end= mid-1
            else:
                start= mid+1
        else:
            if target>a[mid] and target<=a[end]:
                start= mid+1
            else:
                end= mid-1
    return -1


def first_and_last_position_in_sorted_array_34(a,target):
    # [5,7,7,8,8,10], target = 8
    start= 0
    end= len(a)
    l=[-1,-1]
    while end>start:
        mid= start+(end-start)//2

        if a[mid]==target: # 1st time reach, now again check reach in left side
            l[0]= mid
            end= mid
        if target<a[mid]:
            end= mid
        else:
            start= mid+1
    start=0
    end= len(a)
    while end>start:
        mid= start+(end-start)//2

        if a[mid]==target: # 1st time reach, now again check reach in right side
            l[1]=mid
            start= mid+1
        if target<a[mid]:
            end= mid
        else:
            start= mid+1
    return l

def search_insert_35(a,target):
    start= 0
    end= len(a)

    while end>start:
        mid= start+(end-start)//2
        if a[mid]==target:
            return mid
        elif target<a[mid]:
            end= mid
        else:
            start= mid+1
    return start

def sqrt_of_number_using_binary_search_69(num):
    start=0
    end= num+1 # for 0 and 1
    while end>start:
        mid= start+(end-start)//2
        if mid*mid>num:
            end= mid
        else:
            start=mid+1
    return start-1


def Binary_search_in_2D_matrix_74(matrix,target):
    rowStart= 0
    rowEnd= len(matrix)-1
    colEnd= len(matrix[0])-1
    colStart= 0

    while colEnd>=colStart and rowEnd>=rowStart:

        if matrix[rowStart][colEnd]==target:
            return True
        elif matrix[rowStart][colEnd]<target:
            rowStart+=1
        else:
            colEnd-=1
    return False


def search_in_rooted_sorted_array_has_duplicates_81(a,target):

    # remove duplicates
    a= list(dict.fromkeys(a))
    start=0
    end= len(a)-1
    while end>=start:
        mid= start+(end-start)//2

        if a[mid]==target:
            return mid
        if a[mid]>=a[start]:
            if target>=a[start] and target<a[mid]:
                end= mid-1
            else:
                start= mid+1
        else:
            if target>a[mid] and target<=a[end]:
                start=mid+1
            else:
                end= mid-1
    return -1

def minimum_element_in_sorted_rooted_array(a):
    pass
