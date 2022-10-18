
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head= None

    def traverse(self)->None:
        while self.head is not None:
            print(self.head.data)
            self.head= self.head.next
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

        
l= LinkedList()
# l.insertItem(1,5)
# l.insertItem(2,50)
# l.insertItem(3,500)
# l.insertItem(4,5000)
# l.insertItem(5,50000)
l.addItemAtStart(100)
l.addItemAtStart(200)
l.addItemAtStart(300)
l.addItemAtStart(400)
l.addItemAtStart(500)
l.addItemAtStart(500)
l.addItemAtStart(500)
l.addItemAtStart(500)
l.addItemAtStart(600)
l.addItemAtStart(3)
# l.traverse()
# l.removeItem(500)
# l.removeElementByPos(1)
# l.reverselinkedList()
# l.traverse()
# print(l.isPalindrome())
l.countsNode()
# l.searchElement(4)
# l.midOfLinkedList()
