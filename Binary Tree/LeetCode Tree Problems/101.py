class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right =None
        self.data=data
class BinaryTree:
    def symmatricTree(self,root):
        def dfs(r1,r2):
            if(r1 is None and  r2 is None):
                return True
            if(r1 is None or r2 is None):
                return False
            if(r1.data==r2.data):
                return dfs(r1.left,r2.right) and dfs(r1.right,r2.left)
            return False
        return dfs(root.left,root.right)

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
# n1.left=n3
# n1.right=n4
# n2.left=n3
# n2.right=n6
b1=BinaryTree()
t=Node(1)

n11=Node(2)
n12=Node(3)
t.left=n11
t.right=n12

n55=Node(5)
n55.left=tree
n55.right=t
print(b.symmatricTree(n55))
