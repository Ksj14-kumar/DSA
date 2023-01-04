class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right =None
        self.data=data
class BinaryTree:
    def getRightMostNode(self,l,c):
        while l.right is not None and l.right !=c:
            l= l.right
        return l

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

    def RecoverBinarySearchTree(self,root):
        curr= root
        pre,a,b=None,None,None
        while curr is not None:
            left= curr.left
            if(left is None):
                if(pre is not None and pre.data>curr.data):
                    if(a is None):
                        a=pre
                    b=curr
                pre=curr
                curr=curr.right

            if(left is not None):
                rightMostNode= self.getRightMostNode(left,curr)
                if(rightMostNode.right is None):
                    #cretae threade
                    rightMostNode.right=curr
                    curr=curr.left
                else:
                    # break the link
                    rightMostNode.right=None
                    if(pre is not None and pre.data>curr.data):
                        if(a is None):
                            a=pre
                        b=curr
                    pre=curr
                    curr= curr.right

        if(a is not None):
            a.data,b.data=b.data,a.data
        return root

b=BinaryTree()
tree=Node(3)
n1=Node(1)
n2=Node(4)
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
n2.left=n3
# n2.right=n6
