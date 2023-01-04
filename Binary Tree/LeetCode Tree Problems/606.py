def StringfromBinaryTree(root):
    def dfs(root):
        if(root is None):
            return ""
        str1=str(root.data)
        if(root.left is not None):
            str1 +="("+str(dfs(root.left))+")"
        if(root.right is not None):
            if(root.left is None):
                str1 +="()"
            str1+="("+str(dfs(root.right))+")"
        return str1
    return dfs(root)
