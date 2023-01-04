from heapq import heappush, heappop

class Node:
    def __init__(self,data) -> None:
        self.next=None
        self.val= data



class LinkedList:

    def merge_two_sorted_list_method_1(self,l1,l2):
        "Simply iteration"
        if l1 is None and l2 is None:
            return 
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        dummy= Node(-1)
        pre=dummy
        while l1 is not None and l2 is not None:
            if l1.val>l2.val:
                pre.next= l2
                pre= pre.next
                l2= l2.next
            else:
                pre.next= l1
                pre=pre.next
                l1=l1.next
        while l1 is not None:
            pre.next= l1
            pre= pre.next
            l1= l1.next
        while l2 is not None:
            pre.next= l2
            pre= pre.next
            l2= l2.next
        return dummy.next

    def merge_two_sorted_list_method_2(self,l1,l2):
        "using heap data structure"
        if l1 is None and l2 is None:
            return 
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        q=[]
        for l in [l1,l2]:
            while l is not None:
                heappush(q,l.val)
                l= l.next

        dummy= Node(-1)
        pre= dummy
        while len(q):
            rm= heappop(q)
            pre.next= Node(rm)
            pre= pre.next
        return dummy.next


        







        
