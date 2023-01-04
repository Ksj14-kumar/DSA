class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right =None
        self.data=data
class BinaryTree:
    def InorderTraversal_94(self,root):
        def dfs(root,inorder):
            if(root is None):
                return 
            dfs(root.left,inorder)
            inorder.append(root.data)
            dfs(root.right,inorder)
            return inorder
        inorder=[]
        dfs(root,inorder)
        return inorder
    def BinarSearchTreeIsBalanced(self,root):
        def height(root):
            if(root is None):
                return 0
            l= height(root.left)
            r= height(root.right)
            if(l==-1):
                return -1
            if(r==-1):
                return -1
            if(abs(l-r)>1):
                return -1
            return max(l,r)+1

        def dfs(root):
            if(root is None):
                return True
            if(height(root)==-1):
                return False
            return True
        return dfs(root)        

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
n6.left=n7
n7.left=n8
n8.left=n9
# b1=BinaryTree()
# t=Node(1)
# n11=Node(20)
# n12=Node(3)
# t.left=n11
# t.right=n12

inorder=[3,9,20,15,7]
preorder=[1,2,3,4,5,6]
print(b.BinarSearchTreeIsBalanced(tree))
