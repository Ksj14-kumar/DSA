class Node:
    def __init__(self,data) -> None:
        self.data= data
        self.next= None
class LinkedList:
    def __init__(self) -> None:
        self.head= None
    def traverse(self)->None:
        temp= self.head
        while temp:
            print(temp.data)
            temp= temp.next
    def addItemAtBigging(self, item)->None:
        newNode= Node(item) #make a newNode
        if(self.head is None): #head is none make newNode as Head
            self.head= newNode #set newNode as Head
            return 
        newNode.next=self.head
        self.head=newNode
    def addItemAtLast(self,data)->None:
        newNode= Node(data)
        if(self.head is None):
            self.head= newNode
            return
        temp= self.head
        while temp.next is not None:
            temp= temp.next
        temp.next= newNode
    def addItemAtPosition(self,pos,item)->None:
        newNode= Node(item)
        if(pos<1):
            return 
        elif(pos==1):
            #at node at starting
            newNode.next= self.head
            self.head= newNode
        else:
            temp= self.head
            for _ in range(1,pos-1):
                if(temp is not None):
                    temp= temp.next

            if(temp is not None):
                newNode.next= temp.next
                temp.next=newNode
    def deleteFirstNode(self):
        if(self.head is not None):
            temp= self.head # store heade into temp variable
            self.head= self.head.next #make a next head node
            temp= None #delete a temp node
    def deleteLastNode(self):
        if(self.head is not None):
            temp= self.head
            while temp.next.next is not None:
                temp= temp.next
            lastNode= temp.next
            temp.next= None
            lastNode= None
    def deleteNodeByPos(self, pos):
        if(pos<1):
            return 
        elif(pos==1 and self.head is not None):
            deleteNode= self.head
            self.head= self.head.next
            deleteNode= None
        else:
            temp = self.head
            for _ in range(1,pos-1):
                if(temp is not None):
                    temp= temp.next
            if(temp is not None):
                deleteN= temp.next
                temp.next= temp.next.next
                deleteN= None
    def deleteAllNode(self):
        if(self.head is None):
            return
        self.head= None
l= LinkedList()
# n1 = Node(56)
# n2 = Node(5)
# n3 = Node(6)
# n4 = Node(50)
# n5 = Node(93)
# l.head= n1
# n1.next= n2
# n2.next= n3
# n3.next= n4
# n4.next= n5
l.addItemAtBigging(100)
l.addItemAtBigging(200)
l.addItemAtBigging(300)
l.addItemAtLast(500)
l.addItemAtPosition(4,2500)
l.addItemAtPosition(2,60000)
l.deleteFirstNode()
l.deleteFirstNode()
l.deleteLastNode()
l.addItemAtBigging(2000)
l.addItemAtBigging(3000)
l.addItemAtBigging(4000)
l.addItemAtBigging(5000)
l.deleteNodeByPos(2)
l.deleteNodeByPos(3)
# l.deleteAllNode()
l.traverse()
