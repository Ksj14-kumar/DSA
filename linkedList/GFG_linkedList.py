

class Node:
    def __init__(self,data):
        self.data= data
        self.next=None
    
class LinkedList:
    
    def addAtLast(self,value):
        pass

    def traverList(self,head):
        temp= head
        while temp is not None:
            print(temp.data,end=" ")
            temp= temp.next
        

    def deleteNodeByPos(self,head,pos):
        if(head is None):
            return 
        if(pos==0):
            self.traverList(head)
            return head
        if(pos==1):
            self.traverList(head)
            print()
            head=head.next
            self.traverList(head)

        if(pos>1):
            curr=head
            for _ in range(1,pos-1):
                curr=curr.next

            curr.next=curr.next.next
            self.traverList(head)
    





            




l= LinkedList()
n1= Node(1)
n2= Node(1)
n3= Node(2)
n4= Node(2)
n5= Node(4)
a=LinkedList()
a=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
# n5.next
# l.deleteNodeByPos(a,2)
# l.removeAllDuplicatesFromSortedList(a)
