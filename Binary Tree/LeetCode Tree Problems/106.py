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
    def binaryTreeFromInOrderAndPostOrderTraversal(self,inorder,postorder):
        def dfs(inorder,postorder,in_start,in_end,post_start,post_end):
            if(in_start>in_end):
                return
            index= in_start
            while inorder[index] !=postorder[post_end]:
                index +=1
            lrange= index-in_start

            newNode=Node(postorder[post_end])
            newNode.left=dfs(inorder,preorder,in_start,index-1,post_start,post_start+lrange-1)
            newNode.right= dfs(inorder,postorder,index+1,in_end,post_start+lrange,post_end-1)
            return newNode
        return dfs(inorder,postorder,0,len(inorder)-1,0,len(postorder)-1)
        

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
preorder=[9,15,7,20,3]
result=b.binaryTreeFromInOrderAndPostOrderTraversal(inorder,preorder)
print(b.InorderTraversal_94(result))
