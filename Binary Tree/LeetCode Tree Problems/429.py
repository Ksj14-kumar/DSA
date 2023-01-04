class Node:
    def __init__(self,data):
        self.data= data
        self.children=[]

class GenericTree:
    def ConstructGenericTree(self,a):
        " from this type array=10,20,50,-1,60,-1,-1,30,70,-1"
        stack=[]
        root=None
        for i in range(len(a)):
            if(a[i]==-1):
                stack.pop()
            else:
                newNode=Node(a[i])
                if(len(stack)>0):
                    top= stack[-1]
                    top.children.append(newNode)
                    stack.append(newNode)
                else:
                    # initial stage when single stack is empty
                    root=newNode
                    stack.append(root)
        return root

    def displayGenericTree(self,root):
        if(root is None):
            return 
        def dfs(root,path):
            path.append(root.data)
            for child in root.children:
                dfs(child,path)
            return path

        path=[]
        dfs(root,path)
        return path
    def LevelOrderTraversal(self,root):
        if(root is None):
            return 
        q=[]
        q.append(root)
        ans=[]
        while len(q)>0:
            size=len(q)
            small=[]
            while size>0:
                rm= q.pop(0)
                small.append(rm.val)
                for child in rm.children:
                    q.append(child)
                size-=1
            ans.append(small)
        return ans


a=[10,20,-1,30,50,-1,60,-1,-1,40,-1,-1]
g= GenericTree()

print(g.displayGenericTree(g.ConstructGenericTree(a)))