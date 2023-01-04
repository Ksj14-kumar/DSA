

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

    def UniqueBinarySearchTrees_96(self,n):
        """number of unique BST from 1-n numbers=factorial(2*n)/factorial(n+1)*factorial(n)"""
        def factorial(n):
            if(n==0):
                return 1
            return n*factorial(n-1)
        upper= factorial(2*n)
        down= factorial(n+1)*factorial(n)
        return upper//down

    def UniqueBinarySearchTrees_95(self,n):
        def makeBinaryTree(start,end):
            array=[]
            if(start>end):
                array.append(None)
                return array
            for i in range(start,end+1):
                leftArrayRange= makeBinaryTree(start,i-1)
                rightArrayRange=makeBinaryTree(i+1,end)
                for l in leftArrayRange:
                    for r in rightArrayRange:
                        newNode= Node(i)
                        newNode.left=l
                        newNode.right=r
                        array.append(newNode)
            return array
        return makeBinaryTree(1,n)
                    



    

b=BinaryTree()
tree=Node(0)
n1=Node(1)
n2=Node(2)
n3=Node(3)
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
n2.left=n5
n2.right=n6

# print(b.InorderTraversal_94(tree))
# print(b.UniqueBinarySearchTrees_96(4))
print(b.UniqueBinarySearchTrees_95(12))
    



        

    
    