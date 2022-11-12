class Node:
    def __init__(self,item):
        self.data= item
        self.leftChild= None
        self.rightChild= None

    def is_Full_binary_Tree(self,head):
        if(head is None):
            return True
        if(head.leftChild is None and head.rightChild is None):
            return True
        if(head.leftChild is not None and head.rightChild is not None):
            return self.is_Full_binary_Tree(head.leftChild) and self.is_Full_binary_Tree(head.rightChild)
        return False




n1= Node(1)
n1.leftChild=Node(2)
n1.rightChild = Node(3)
n1.leftChild.leftChild=Node(4)
n1.leftChild.rightChild= Node(5)
n1.rightChild.leftChild= Node(6)
n1.rightChild.rightChild= Node(7)
print(n1.is_Full_binary_Tree(n1))