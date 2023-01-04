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
    def binaryTreeFromSortedArray(self,a):
        def dfs(a,start,end):
            if(start>end):
                return
            if(end>start):
                mid= start+(end-start)//2
                newNode=Node(a[mid])
                newNode.left= dfs(a,start,mid)
                newNode.right=dfs(a,mid+1,end)
                return newNode
        return dfs(a,0,len(a))
                

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

inorder=[3,9,20,15,7]
preorder=[1,2,3,4,5,6]
# print(b.binaryTreeFromSortedArray(preorder))
print(b.InorderTraversal_94(b.binaryTreeFromSortedArray(preorder)))
