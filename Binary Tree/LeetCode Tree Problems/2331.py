def EvaluateBooleanBinaryTree(root):
    def dfs(root):
        if(root.left is None and root.right is None):
            return root.data
        l= dfs(root.left)
        r= dfs(root.right)
        if(root.val==2):
            return l or r
        if(root.val==3):
            return l and r

    return dfs(root)