

def ValidateBinarySearchTree(root):
    "Method-1, using inorder traversal"
    """
    def dfs(root,inorder):
        if(root is None):
            return
        dfs(root.left,inorder)
        inorder.append(root.val)
        dfs(root.right,inorder)
        return inorder
    inorder=[]
    temp=inorder
    dfs(root,inorder)
    if(temp==sorted(inorder)):
        return True
    return False
    """
    "M-2, using morrise traversal"

    # def getRightMostNode(c,l):
    #     while l.right is not None and l.right !=c:
    #         l= l.right
    #     return l
    # def morris(root):
    #     curr= root
    #     pre=None
    #     while curr is not None:
    #         left= root.left
    #         if(left is None):
    #             if(pre is not None and pre.data>curr.data):
    #                 return False
    #             pre=curr
    #             curr= curr.right

    #         else:
    #             rightMostNode= getRightMostNode(curr,left)
    #             if(rightMostNode.right is None):
    #                 # create thread
    #                 rightMostNode.right=curr
    #                 curr=curr.left
    #             else:
    #                 # break threade
    #                 rightMostNode.right=None
    #                 if(pre is not None and pre.data>curr.data):
    #                     return False
    #                 pre=curr
    #                 curr=curr.right
    #         return True
    #     return morris(root)
