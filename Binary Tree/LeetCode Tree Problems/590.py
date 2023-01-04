import random
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
    def PostOrderTraversal(self,root):
        if(root is None):
            return 
        def dfs(root,path):
            for child in root.children:
                dfs(child,path)
            path.append(root.data)
            return path
        path=[]
        dfs(root,path)
        return path
    def nodeToRootPath(self,root,val):
        def dfs(root,path,paths,val):
            path.append(root.data)
            if(root.data==val):
                paths.append(path.copy())
            for child in root.children:
                dfs(child,path,paths,val)
            path.pop()
            return 
        path,paths=[],[]
        dfs(root,path,paths,val)
        print(paths,path)

    def lowestCommonAncesterBetweenTwoNodes(self,root,v1,v2):
        def dfs(root,path,paths,v1,v2):
            path.append(root.data)
            if(root.data==v1 or root.data==v2):
                paths.append(path.copy())
            for child in root.children:
                dfs(child,path,paths,v1,v2)
            path.pop()
            return
        path,paths=[],[]
        dfs(root,path,paths,v1,v2)
        value=None
        if(v1==v2):
            value=paths[0][len(paths)-3]
        else:
            a,b=paths
            i=len(a)-1
            j= len(b)-1
            while i !=0  and j!=0:
                if(a[i]==b[i]):
                    value=a[i]
                    break
                i-=1
                j -=1
        print(value)
        return value

    def distanceBetweenTwoNodes(self,root,v1,v2):
        def dfs(root,path,paths,v1,v2):
            path.append(root.data)
            if(root.data==v1 or root.data==v2):
                paths.append(path.copy())
            for child in root.children:
                dfs(child,path,paths,v1,v2)
            path.pop()
            return 
        path,paths=[],[]
        dfs(root,path,paths,v1,v2)
        print(paths)
        a,b=paths
        i=len(a)-1
        j=len(b)-1
        count =0
        while i!=0 and j!=0:
            if(a[i]==b[j]):
                break
            count +=1
            i-=1
            j-=1
        print(count+1)
        return count+1





a=[10,20,50,-1,60,-1,70,-1,-1,30,80,120,-1,130,-1,140,-1,-1,20,-1,100,-1,40,110,-1,-1,-1]
g= GenericTree()

print(g.PostOrderTraversal(g.ConstructGenericTree(a)))
# g.nodeToRootPath(g.ConstructGenericTree(a),140)
g.distanceBetweenTwoNodes(g.ConstructGenericTree(a),140,100)


print(random.choice([1,4,2,3,5]))