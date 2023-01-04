class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data

def MaximumBinaryTreeII(root,val):
    if(root.val>val):
        root.right= MaximumBinaryTreeII(root.right,val)
        return root

    newNode=Node(val) #Node class
    newNode.left=root
    return newNode