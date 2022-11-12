



class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head= None
        self.th=None
        self.tt=None

    def traverse(self)->None:
        while self.head is not None:
            print(self.head.data)
            self.head= self.head.next
    def traverseList(self,l):
        curr=l
        while curr is not None:
            print(curr.data,end=" ")
            curr= curr.next
        print()
        return 

    def addItemAtStart(self,item):
        newNode= Node(item)
        newNode.next= self.head
        self.head= newNode
    def addItemAtLast(self,item):
        newNode= Node(item)
        if(self.head is None):
            newNode.next= self.head
            self.head= newNode
        temp= self.head
        while temp.next is not None:
            temp= temp.next
        temp.next= newNode

    def insertItem(self,pos,item)->None:
        newNode= Node(item)
        if(pos<1):
            return 
        elif(pos==1):
            newNode.next= self.head
            self.head= newNode
        else:
            temp= self.head
            for _ in range(1,pos-1):
                if(temp is not None):
                    temp=temp.next
            
            if(temp is not None):
                newNode.next= temp.next
                temp.next= newNode
    def removeItem(self,item):
        "delete same items by key"
        if(self.head is None):
            return 
            
            # self.head.next= self.head.next.next
        # Case-1: when item at starting position
        while (self.head is not None and self.head.data==item):
            self.head= self.head.next
        # Case-2: when item in middle
        temp = self.head
        if(temp is not None):

            while temp.next is not None:
                if(temp.next.data==item):
                    temp.next= temp.next.next
                else:
                    temp= temp.next
    
    def removeElementByPos(self,pos)->None:
        if(self.head is None):
            return
        elif(pos==1):
            deleteNode= self.head
            self.head= self.head.next
            deleteNode= None
        else:
            temp= self.head
            for _ in range(1,pos-1):
                if(temp is not None):
                    temp= temp.next
            if(temp is not None):
                deleteNode= temp.next
                temp.next= temp.next.next
                deleteNode= None
    def reverselinkedList(self):
        if(self.head is None or self.head.next is None):
            return
        pre= None
        curr= self.head
        forw= None
        while curr is not None:
            forw= curr.next #backup
            curr.next= pre #link
            pre= curr
            curr= forw
        # print([pre])
        self.head= pre

    def reversedLinkedAddFirst(self,l):
        if(l is None or l.next is None):
            return l
        curr=l
        while curr is not None:
            forw=curr.next
            curr.next=None
            self.AddFirst(curr)
            curr=forw
        # return self.th
        while self.th is not None:
            print(self.th.data,end=" ")
            self.th=self.th.next


    def AddFirst(self,l):
        
        if(self.th is None):
            self.th,self.tt=l,l
        else:
            l.next=self.th
            self.th=l

    def countsNode(self):
        if(self.head is None):
            return 
        count =0
        while self.head is not None:
            self.head=self.head.next
            count +=1
        print(count)
    def searchElement(self, item):
        pass
        # if(self.head is None or self.head.next is None):
        #     return self.head
        # temp = self.head
        # count =0
        # while temp.next is not None:
        #     if(temp.data.next==item):
        #         print(count)
        #         break
        #     else:
        #         temp = temp.next

    def midOfLinkedList(self):
        if(self.head is None or self.head.next is None):
            return self.head
        currentPos= self.head
        forwardPos= self.head
        while forwardPos.next is not None and forwardPos.next.next is not None:
            currentPos= currentPos.next
            forwardPos= forwardPos.next.next
        # self.head=currentPos
        # return self.head
        # print(currentPos.data)
        return currentPos
    def midOfLinkedListWithParameters(self,head):
        if(head is None or head.next is None):
            return head
        slow= head
        fast= head
        while fast.next is not None and fast.next.next is not None:
            fast= fast.next.next
            slow= slow.next
        return slow
    def isPalindrome(self):
        if(self.head is None or self.head.next is None):
            return True
        midPoint= self.midOfLinkedList(self.head)
        newHead= midPoint.next
        midPoint.next= None
        newHead= self.reverselinkedList(self.head)
        p1= self.head
        p2= newHead
        bool= True
        while p1 is not None and p2 is not None:
            if(p1.data !=p2.data):
                bool=False
                break
            p1= p1.next
            p2= p2.next
        return bool
    def detectCycle(self):
        if(self.head is None or self.head.next is None):
            return False # because single item not cycle
        s= self.head
        f= self.head
        while f.next is not None and f.next.next is not None:
            s= s.next
            f=f.next.next
            if(s==f):
                return True
        return False
    
    def intersection(self,l1,l2):
        if(l1 is None or l2 is None):
            return 
        #calculate tail of list-1

        tail= l1
        while tail.next is not None:
            tail= tail.next
        #now attached l2 to with l1
        tail.next= l2
        #now it become cycle

        ans= self.StartCycle(l1)

        return ans
    def StartCycle(self,head):
        if(head is None or head.next is None):
            return head
        
        # set 2 pointer on head
        slow= head
        fast = head
        # move pointers, slow with one step and fast with two step
        while fast.next is not None and fast.next.next is not None:

            #move
            slow= slow.next
            fast= fast.next.next
            #break if slow and fast denote same head
            if(slow==fast):
                break

        # if slow and fast not same when condition false from while loop
        if(slow !=fast):
            return
        #again set pointer slow and fast on head and now this is move by one step only
        slow= head
        fast= fast
        while fast != slow:
            fast= fast.next
            slow= slow.next
        return slow
    def removeDuplicatesFromSortedList(self,l):
        if(l is None or l.next is None):
            return 
        temp= l
        while temp.next is not None:
            if(temp.data ==temp.next.data):
                temp.next= temp.next.next
            else:
                temp = temp.next
        return l
    def mergeTwoSortedLinkedList(self,l1,l2):
        if(l1 is None or l2 is None):
            #if anyone list is empty then return non empty list
            if(l1 is None):
                return l2
            else:
                return l1
            
        # now check first small item of any list, and put into temp list
        if(l1.data>l2.data):
            temp= head =Node(l2.data)
            l2= l2.next
        else:
            temp= head= Node(l1.data)
            l1= l1.next

        while l1 is not None and l2 is not None:
            if(l1.data>l2.data):

                temp.next= Node(l2.data)
                l2= l2.next
            else:
                temp.next= Node(l1.data)
                l1= l1.next
            temp= temp.next
        while l1 is not None:
            temp.next= Node(l1.data)
            l1= l1.next
            temp= temp.next
        while l2 is not None:
            temp.next= Node(l2.data)
            l2= l2.next
            temp= temp.next

        t= head
        while t is not None:
            print(t.data,end=" ")
            t= t.next

    def removeDuplicatesFromSortedList(self,l):
        if(l is None or l.next is None):
            return l
        temp= l
        while temp.next is not None:
            if(temp.next.data==temp.next.data):
                temp.next= temp.next.next
            else:
                temp=temp.next

        t= l
        while t is not None:
            print(t.data,end=" ")
            t= t.next

    def linkedListLength(self,l):
        count =0
        temp= l
        while temp is not None:
            temp= temp.next
            count +=1
        return count
    
    def reversed(self,l):
        if(l is None or l.next is None):
            return l
        forw= None
        pre= None
        curr= l
        while curr is not None:
            forw= curr.next
            curr.next= pre
            pre= curr
            curr= forw
        return pre
    def devide(self,l,k):
        if(l is None or l.next is None):
            return l
        temp =l
        while k>1:
            temp=temp.next
            k -=1
        newHead= temp.next
        temp.next=None
        return [self.reversed(l),self.reversed(newHead)]

        

    def rotateListFromKthPos(self,list1,k):
        if(list1 is None or list1.next is None):
            return list1        
        if(k==0):
            return list1
        l= self.linkedListLength(list1)
        pos = k%l
        leftPos= l-pos
        if(pos==0):
            return list1
        curr= list1
        for _ in range(leftPos-1):
            curr= curr.next
        
        newHead= curr.next
        curr.next=None #without this create cycle
        tail= newHead
        while tail.next is not None:
            tail= tail.next
        tail.next= list1
        self.traverseList(newHead)
    def addTwoNumber(self,l1,l2):
        if(l1 is not None or l2 is not None):
            if(l1 is None):
                return l2
            if(l2 is None):
                return l1
            
        head= Node(-1)
        temp= head
        c1= l1
        c2= l2
        carry=0
        while c1 is not None or c2 is not None:

            sum_value= carry #resign the sum_value by an carry
            if(c1 is not None):
                sum_value +=c1.data
                c1= c1.next
            if(c2 is not None):
                sum_value +=c2.data
                c2= c2.next
            ld= sum_value%10
            carry=sum_value//10
            temp.next=Node(ld)
            temp= temp.next
        if(carry>0):
            temp.next= Node(carry)
            
        return head.next

    def removeNthNodeFromLast(self,list1,k):
        s=list1
        f=list1
        for i in range(k):
            #handle when length 1 or 2
            if(f.next is None):
                if(i==k-1):
                    list1=list1.next
                    return list1
                return list1
            f= f.next

        while f.next is not None:
            s=s.next
            f=f.next
        if s.next is not None:
            s.next= s.next.next
        self.traverseList(list1)
        return list1
    def removeAllDuplicatesFromSortedList(self,head):
        if(head is None or head.next is None):
            return head
        dummy=Node(-1)
        pre= dummy
        pre.next= head
        curr= head.next
        while curr is not None:
            isloopRun= False
            while curr is not None and pre.next.data==curr.data:
                isloopRun=True
                curr= curr.next
            if(isloopRun):
                pre.next=curr
            else:
                pre= pre.next
            if(curr is not None):
                curr= curr.next
        self.traverList(dummy.next)
        return dummy.next

    def reversedMiddleRangeList(self,head,l,r):
        if(head is None or head.next is None):
            return head
        dummy=Node(-1)
        dummy.next=head
        d1=dummy
        for _ in range(l-1):
            d1= d1.next

        curr= d1.next
        n=r-l
        pre=None
        while n>=0:
            forw= curr
            curr.next=pre
            pre=curr
            curr=forw
            n=n-1 
        d1.next.next=forw
        d1.next=pre
        self.traverseList(dummy.next)
        return d1.next
    def splitLinkedListInParts(self,head,p):
        l1=[]
        # if(head is None):
        #     for _ in range(p):
        #         l1.append(head)
        l= self.linkedListLength(head)
        division=l//p
        rem= l %p
        pre=None
        curr=head        
        for _ in range(p):
            increamentParts=division 
            if(rem>0):
                rem -=1
                increamentParts +=1
            l1.append(curr)
            for _ in range(increamentParts):
                pre=curr
                curr=curr.next
            if(pre is not None):
                pre.next=None
        for i in l1:
            
            self.traverseList(i)
            print()
        return l1
    def oddEvenList(self,head):
        if(head is None or head.next is None):
            return head
        head_even, odd, even= head.next, head, head.next
        od=odd
        ev= even
        while od is not None and ev is not None and ev.next is not None:
            od.next= ev.next
            od= od.next
            if(od):
                ev.next= od.next
                ev= ev.next
        self.traverseList(even)
        self.traverseList(odd)
        od.next= head_even
        self.traverseList(head)
        return head
    def mergeTwoUnsortedLinkedList(self,list1, list2):
        if(list1 is None):
            return list2
        if(list2 is None):
            return list1    
        result= None
        if(list1.data>=list2.data):
            result=list2
            result.next= self.mergeTwoUnsortedLinkedList(list1, list2.next)
        else:
            result= list1
            result.next= self.mergeTwoUnsortedLinkedList(list1.next,list2)
        return result
    def mergeSortForLinkedList(self,head):
        if(head is None or head.next is None):
            return head
        mid= self.midOfLinkedListWithParameters(head)
        newHead=mid.next
        mid.next=None
        left_side= self.mergeSortForLinkedList(head)
        right_side= self.mergeSortForLinkedList(newHead)
        mergeLinkedList= self.mergeTwoUnsortedLinkedList(left_side,right_side)
        # self.traverseList(mergeLinkedList)
        return mergeLinkedList
    def removeZeroSumConsecutiveNode(self,head):
        if(head is None or head.next is None):
            return head
        sorted_linked_list= self.mergeSortForLinkedList(head)
        temp= sorted_linked_list
        forw=None
        dummy1=Node(-1)
        d1=dummy1
        while temp is not None:
            if(temp.next.data>0):
                forw=temp.next
                temp.next=None
                break
            temp= temp.next
        # self.traverseList(sorted_linked_list)
        # self.traverseList(forw)
            
        left_side= sorted_linked_list
        right_side= forw
        tail=forw
        while tail.next is not None:
            tail=tail.next
        tail.next =None
        self.traverseList(tail)
        self.traverseList(left_side)
        self.traverseList(right_side)
        while right_side is not None:
            # print(right_side.data)
            while left_side is not None:
                # print("e")
                if(-(right_side.data) !=left_side.data):
                    d1.next= right_side
                    d1= d1.next
                left_side= left_side.next
            left_side=forw
            right_side= right_side.next
        return
    def swapNodesOnKthPositionFromLastandFirst(self,head,l):
        if(head is None):
            return head
        # if(l==r):
        #     return head
        first=head
        last=head
        self.traverseList(head)
        print()
        for _ in range(1,l):
            first=first.next
        newPointer=first
        pre=None
        while newPointer is not None:
            newPointer= newPointer.next
            
            pre=last
            last=last.next
        self.traverseList(pre)
        print()
        first.data,pre.data=pre.data,first.data
        self.traverseList(head)
        return head
    def swapNodesRandomPosition(self,head,l,r):
        if(head is None):
            return head
        last,first=head,head
        LinkedList_length=self.linkedListLength(head)
        for _ in range(1,l):
            first= first.next
        for _ in range(1,LinkedList_length-r+1):
            last= last.next
        first.data, last.data= last.data, first.data
        self.traverseList(head)
        return head

    def swapNodesWithPairWise(self,head):
        if(head is None or head.next is None):
            return head
        curr=head
        while(curr is not None and curr.next is not None):
            if(curr.data !=curr.next.data):
                curr.data,curr.next.data=curr.next.data,curr.data
            curr=curr.next.next
        self.traverseList(head)
        return head
    def findMaximumValue(self,head):
        if(head is None and head.next is None):
            return head
        max= 0
        curr= head
        while curr is not None:
            if(curr.data>max):
                max=curr.data
            curr=curr.next
        print(max)
        return
    def findNextGreaterElement(self,head):
        """next greater element in TC=O(n) using stack"""
        dummy=Node(-1)
        pre= dummy
        curr= head
        stack= []
        empty=[]        
        reversed_list= self.reversed(head)
        

        curr= reversed_list
        while curr is not None:
            if(len(stack)==0):
                pre.next = Node(-1)
                pre= pre.next
                stack.append(curr.data)
            elif(len(stack)>0 and curr.data>=stack[-1]):
                while len(stack)>0 and curr.data>=stack[-1]:
                    stack.pop()
                if(len(stack)==0):
                    pre.next= Node(-1)
                    pre= pre.next
                    stack.append(curr.data)
                else:
                    pre.next=Node(stack[-1])
                    pre= pre.next
                    stack.append(curr.data)
            elif(len(stack)>0 and curr.data<stack[-1]):
                pre.next= Node(stack[-1])
                pre= pre.next
                stack.append(curr.data)
            curr= curr.next
        l= self.reversed(dummy.next)
        # l= dummy.next
        while l is not None:
            empty.append(l.data)
            # print(l.data,end=" ")
            l= l.next
        print(empty)
        return 
    def removeNodeWhoseSumK(self,head):
        k=0
        # if(head is None or head.next is None):
        #     return head
        # handle all cases
        root= Node(0)
        root.next= head
        d= dict()
        d[0]= root
        sum=0
        while head is not None:
            sum +=head.data
            if(sum-k in d):
                pre= d[sum-k]
                start= pre
                resum=sum
                sum = sum-k
                while pre !=head:
                    pre= pre.next
                    resum +=pre.data
                    if(pre !=head):
                        d.pop(resum)
                start.next= head.next

            else:
                d[sum]= head
            head= head.next
        self.traverseList(root.next)
    def flattenBinaryTree(self,root):
            if(root.left is not None):
                self.flattenBinaryTree(root.left)
                temp= root.right
                root.right= root.left
                root.left=None
                t= root.right
                while t.right is not None:
                    t= t.right
                t.right= temp
            self.flattenBinaryTree(root.right)
    def sortedNodes(self,pre, next_node):
        if(pre is None or pre.data>=next_node.data):
            next_node.next= pre
            pre= next_node
        else:
            curr= pre
            while curr.next is not None and curr.next.data<next_node.data:
                curr= curr.next
            next_node.next= curr.next
            curr.next=next_node
        return pre
    def InsertionSort(self,head):
        """TC=O(n^2)"""
        if(head is None or head.next is None):
            return head
        pre= None
        curr= head
        while curr is not None:
            forw=curr.next
            pre=self.sortedNodes(pre,curr)
            curr= forw
        head= pre
        self.traverseList(head)
        return head
    
    def shallowCopy(self,head):
        curr= head
        while curr is not None:
            forw=curr.next
            newNode= Node(curr.next)
            curr.next = newNode
            newNode.next= forw
            curr=forw
    def copyrandomPointer(self, head):
        curr= head
        while curr is not None:
            random= curr.random
            if(random):
                curr.next.random= random.next
            curr= curr.next.next
    def extractCopy(self,head):
        dummy= Node(-1)
        pre= dummy
        curr= head
        while curr is not None:
            pre.next= curr.next
            curr.next= curr.next.next
            pre= pre.next
            curr= curr.next
        return dummy.next
    def copyWithRandomPointer(self,head):
        self.shallowCopy(head)
        self.copyrandomPointer(head)
        return self.extractCopy(head)
    
    def mergeListInBetween(self,list1, list2,a,b):
        if(list1 is None):
            return list2
        if(list1 is None):
            return list2
        curr= list1
        pre= list1
        forw= list1
        tail= list2
        for i in range(1,a):
            pre= pre.next
        for _ in range(b):
            forw= forw.next
        while tail.next is not None:
            tail= tail.next
        pre.next= list2
        tail.next= forw.next
        return curr
    def mergeNodeInBetweenZeros(self,head):
        """
        0-1-2-0-3-4-0-6-0 === 0-3-0-7-0-6-0
        """
        if(head is None):
            return head
        dummy= Node(-1)
        pre= dummy
        sum=0
        curr= head
        while curr is not None:
            forw= curr.next
            while forw is not None:
                if(forw.data !=0):
                    sum +=forw.data
                else:
                    break
                forw= forw.next
            if(sum !=0):
                pre.next= Node(sum)
                pre= pre.next
            sum=0
            curr= forw
        return dummy.next

    def segrigateAboutPivateElement(self, head,k):
        if(head is None):
            return head
        dummy1= Node(-1)
        small= dummy1
        dummy2= Node(-1)
        large= dummy2
        curr= head
        pivote= None
        while curr is not None:
            if(curr.data<k):
                small.next = curr
                small=small.next
            elif(curr.data==k):
                pivote= curr
            else:
                large.next= curr
                large= large.next
            curr= curr.next

        small.next= pivote
        pivote.next= dummy2.next
        large.next = None
        self.traverseList(dummy1.next)
        return 



        

    





    



        
        
            




            


        



        
                    
        




    
       
        
        
    

            


       


        
        
            



        
        

    

        
l= LinkedList()
# l.insertItem(1,5)
# l.insertItem(2,50)
# l.insertItem(3,500)
# l.insertItem(4,5000)
# l.insertItem(5,50000)
# l.addItemAtStart(100)
# l.addItemAtStart(200)
# l.addItemAtStart(300)
# l.addItemAtStart(400)
# l.addItemAtStart(500)
# l.addItemAtStart(500)
# l.addItemAtStart(500)
# l.addItemAtStart(500)
# l.addItemAtStart(600)
# l.addItemAtStart(3)
# l.traverse()
# l.removeItem(500)
# l.removeElementByPos(1)
# l.reverselinkedList()
# l.traverse()
# print(l.isPalindrome())
# l.countsNode()
# l.searchElement(4)
# l.midOfLinkedList()
# a= LinkedList()
# b= LinkedList()
# # n1= Node(1)
# # n2= Node(2)
# # n3= Node(3)
# n11= Node(11)
# n12= Node(12)
# n13= Node(13)
# n14= Node(14)
# # a=n1
# # n1.next=n2
# # n2.next=n3
# b.next= n11
# n11.next=n12
# n12.next=n13
# n13.next=n14
# l.mergeTwoSortedLinkedList(b,a)
# c= LinkedList()
# n1=Node(1)
# n2=Node(2)
# n3=Node(12)
# n4=Node(3)
# n5=Node(13)
# n6=Node(23)
# n7=Node(4)
# n8=Node(5)
# n9=Node(6)
# c=n1
# n1.next=n2
# n2.next=n3
# n3.next=n4
# n4.next=n5
# n5.next=n6
# n6.next=n7
# n7.next=n8
# n8.next=n9
# print(l.rotateListFromKthPos(b,2))
# print("\n")
# l.removeDuplicatesFromSortedList(c)
# print(c.rotateListFromKthPos(c,2))
a=LinkedList()
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(-3)
n5=Node(1)
n6=Node(6)
n7=Node(7)
n8=Node(8)
n9=Node(9)
n10=Node(100)
n11=Node(11)
n12=Node(12)
n13=Node(13)
a=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
n7.next=n8
n8.next=n9
n9.next=n10
n10.next=n11
n11.next=n12
n12.next=n13
# l.reversedLinkedAddFirst(a)
# l.rotateListFromKthPos(a,2)
# l.removeNthNodeFromLast(a,1)
# l.reversedMiddleRangeList(a,4,7)
# l.splitLinkedListInParts(a,3)
# l.oddEvenList(a)
# l.removeZeroSumConsecutiveNode(a)
# l.swapNodesOnKthPositionFromLastandFirst(a,4)
# l.swapNodesRandomPosition(a,4,4)
# l.swapNodesWithPairWise(a)
# l.swaptwoNodes(n1,n2)
# l.findMaximumValue(a)
# l.findNextGreaterElement(a)
# l.removeNodeWhoseSumK(a)
# l.mergeSortForLinkedList(a)
# l.InsertionSort(a)
l.segrigateAboutPivateElement(a,3)
