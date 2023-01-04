class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right =None
        self.data=data
class BinaryTree:
    def levelOrderTraversal(self,root):
        if(root is None):
            return 
        q=[]
        q.append(root)
        ans=[]
        while len(q)>0:
            size= len(q)
            small=[]
            while size>0:
                rm= q.pop(0)
                small.append(rm.data)
                if(rm.left is not None):
                    q.append(rm.left)
                if(rm.right is not None):
                    q.append(rm.right)
                size-=1
            ans.append(small)
        return ans

b=BinaryTree()
tree=Node(1)
n1=Node(2)
n2=Node(3)
n3=Node(2)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)
n8=Node(8)
n9=Node(9)
n10=Node(10)
n11=Node(11)
n12=Node(12)
n13=Node(13)
n14=Node(14)
tree.left=n1
tree.right=n2
n1.left=n3
n1.right=n4
n2.left=n3
n2.right=n6
# b1=BinaryTree()
# t=Node(1)
# n11=Node(20)
# n12=Node(3)
# t.left=n11
# t.right=n12

print(b.levelOrderTraversal(tree))
