class Node:
    def __init__(self,key):
        self.data= key
        self.rightChild= None
        self.leftChild= None

    def cal_culate_depth(self,root):
        """calculate depth of a binary tree"""
        d=0
        while root is not None:
            d +=1
            root= root.leftChild
        return d

    def is_perfect_binary_tree(self,root,depth,level=0):
        if(root is None):
            # tree is empty
            return True
        if(root.leftChild is None and root.rightChild is None):
            # when single node
            return depth==level+1
        if(root.leftChild is None and root.rightChild is None):
            return False
        
        return (self.is_perfect_binary_tree(root.leftChild,depth,level+1) and self.is_perfect_binary_tree(root.rightChild,depth,level+1) )


n1 = Node(1)
n1.leftChild= Node(2)
n1.rightChild= Node(3)
n1.leftChild.leftChild= Node(4)
n1.leftChild.rightChild= Node(5)
n1.rightChild.leftChild=Node(6)
# n1.rightChild.rightChild= Node(7)

print(n1.is_perfect_binary_tree(n1,n1.cal_culate_depth(n1)))
