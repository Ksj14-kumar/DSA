def DistributeCoinsinBinaryTree(self,root):
    def dfs(root,res):
        if(root is None):
            return 0
        l= dfs(root.left,res)
        r= dfs(root.right,res)
        res[0]+=abs(l)+abs(r)
        return root.val-1+l+r
    res=[0]
    dfs(root,res)
    return res[0]