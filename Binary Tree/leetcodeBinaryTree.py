from selectors import EpollSelector


class Node:
    def __init__(self,item):
        self.data= item
        self.left= None
        self.right= None


class Sorting:
    def mergeSort(self,a):
        if(len(a)>1):
            mid= len(a)//2
            left= a[:mid]
            right= a[mid:]
            self.mergeSort(left)
            self.mergeSort(right)
            i=j=k=0
            while i<len(left) and j<len(right):
                if(left[i]>right[j]):
                    a[k]= right[j]
                    j +=1
                else:
                    a[k]= left[i]
                    i +=1
                k +=1
            while i<len(left):
                a[k]= left[i]
                i +=1
                k +=1
            while j<len(right):
                a[k]= right[j]
                j +=1
                k +=1
            return a
        return a
    

    
class BinaryTree():
    
    def PreOrderTraversal(self,root)->list[int]:
        def dfs(root,path):
            if(root is None):
                return
            path.append(root.data)
            self.PreOrderTraversal(root.left,path)
            self.PreOrderTraversal(root.right, path)
            return path
        path= []
        dfs(root,path)
        return path
    def InorderTraversal(self,root,path)->list[int]:
        def dfs(root, path):
            if(root is None):
                return
            dfs(root.left, path)
            path.append(root.data)
            dfs(root.right, path)
            return path
        path= []
        dfs(root,path)
        return path
    def PostOrderTraversal(self,root, path)->list[int]:
        def dfs(root, path):
            if(root is None):
                return 
            dfs(root.left,path)
            dfs(root.right,path)
            path.append(root.data)
            return path
        path= []
        dfs(root,path)
        return path
    def binaryTreePaths(self,root)-> list[int]:
        def dfs(root, str,path,paths):
            if(root is None):
                return 
            # form-node: 1->2->3->4
            str +=f"{root.data}->" if root.left is not None or root.right is not None else f"{root.data}"
            path.append(str)
            if(root.left is None and root.right is None):
                paths.append(path[-1]) 
            dfs(root.left,str, path,paths)
            dfs(root.right, str, path,paths)
            path.pop()
            return paths
        path=[]
        paths=[]
        str=""
        dfs(root,str,path,paths)
        return paths
    def maxDepth(self, root)->int:
        if(root is None):
            return 0
        left = self.maxDepth(root.left)
        right= self.maxDepth(root.right)
        return max(left, right)+1
    def reverseTree(self,root):
        if(root is None):
            return 
        self.reverseTree(root.left)
        self.reverseTree(root.right)
        root.left, root.right= root.right, root.left
        return root
    def SumofRootToLeafBinaryNumbers(self,root)->int:
        def dfs(root, s, path, paths):
            if(root is None):
                return 0
            s +=str(root.data)
            path.append(s)
            if(root.left is None and root.right is None):
                paths.append(path[-1])
            dfs(root.left, s, path, paths)
            dfs(root.right, s, path, paths)
            path.pop()
            return paths
        def BinaryToDecimal(n):
            power= 1
            decimal= 0
            while n>0:
                rem= n%10
                n //=10
                decimal +=rem*power
                power *=2
            return decimal
        paths= []
        path= []
        s=""
        dfs(root,s,path,paths)
        sum =0
        for i in paths:
            sum +=BinaryToDecimal(i)
        return sum
    def pathsSum(self,root):
        def dfs(root,path,paths,sum):
            if(root is None):
                return 0
            sum +=root.data
            path.append(sum)
            if(root.left is None and root.right is None):
                paths.append(path[-1])
            dfs(root.left,path,paths,sum)
            dfs(root.right,path,paths,sum)
            return paths
        paths= []
        path= []
        sum=0
        dfs(root,path,paths,sum)
        print(paths)
    def pathSumSecond(self,root,target):
        def dfs(root,s,p,p1):
            if(root is None):
                return 
            s +=f"{root.data} " if root.left is not None or root.right is not None else f"{root.data}"
            p.append(s)
            if(root.left is None and root.right is None):
                p1.append(p[-1])
            dfs(root.left, s,p,p1)
            dfs(root.right,s,p,p1)
        p,p1=[],[]
        s=""
        dfs(root,s,p,p1)
        def calCulate_sum(a):
            sum =0
            for i in a:
                sum +=i
            return sum
        i =0
        new= []
        while i<len(p1):
            intergerList=[int(i) for i in p1[i].split(" ")]
            cal=calCulate_sum(intergerList)
            if(cal==target):
                new.append(intergerList)
            i +=1
        print(new)
    def secondMinimumElement(self,root):
        def dfs(root,a):
            if(root is None):
                return 
            if(root.data not in a):
                a.append(root.data)
            dfs(root.left,a)
            dfs(root.left,a)
        a=[] #unique value of tree
        dfs(root,a)
        value= Sorting.mergeSort(a)
        if(len(value)>=2):
            return value[1]
        return value
    def kthMinimumElement(self,root,k):
        def dfs(root,a):
            if(root is None):
                return
            if(root.data not in a):
                a.append(root.data)
            dfs(root.left,a)
            dfs(root.right,a)
        a= []
        dfs(root,a)
        value= Sorting.mergeSort(a)
        return value[k-1]
    def sameTree(self, root1, root2):
        if(root1 is None):
            return False
        if(root2 is None):
            return True
        elif(root1.data==root2.data):
            return self.sameTree(root1.left,root2.left) and self.sameTree(root1.right, root2.right)
        else:
            return False
    def BinaryTreeTilt(self, root):
        def dfs(root, tilt):
            if(root is None):
                return 0
            left=dfs(root.left,tilt)
            right= dfs(root.right, tilt)
            tilt[0] +=abs(left-right)
            return left+right+root.data
        tilt= [0]
        dfs(root, tilt)
        return tilt[0]
    def symetric(self, root):
        if(root is None):
            return True
        def dfs(r1, r2):
            if(r1 is None and r2 is None):
                return True
            elif(r1 is None or r2 is None):
                return False
            else:
                return r1.data==r2.data and dfs(r1.left, r2.right) and dfs(r1.right, r2.left)
        return dfs(root.left, root.right)
    def balanced(self,root):
        def getHeight(root):
            if(root is None):
                return 0
            left= getHeight(root.left)
            right= getHeight(root.right)
            if(left==-1):
                return -1
            if(right==-1):
                return -1
            return max(left, right)+1
        if(root is None):
            return True
        if(getHeight(root)==-1):
            return False
        return True
    def isCousins(self,root,x):
        def pathOfNode(root,value,paths,path):
            if(root is None):
                return 0
            path.append(root.data)
            value= root.data==value or pathOfNode(root.left,value,paths,path) or pathOfNode(root.rightvalue,paths,path)
            if(value):
                paths.append(path.copy())
            path.pop()
            return value

        if(root is None):
            return True
        path=[]
        paths=[]
        pathOfNode(root,x,path,paths)
        print(paths)        
    def levelOrderTraversal(root):
        if(root is None):
            return 
        q= []
        q.append(root)
        ans=[]
        while len(q)>0:
            size= len(q)
            small=[]
            while size>0:
                rm= q.pop(0)
                small.append(rm.data)
                if(rm.left is not None):
                    q.append(rm.left)
                if(rm.right is not None):
                    q.append(rm.right)
                size -=1
            ans.append(small)
        return ans

    def mergeTwoBinary(self,root1, root2):
        if(root1 is None):
            return root2
        if(root2 is None):
            return root1
        root1.data= root1.data+root2.data
        l= self.mergeTwoBinary(root1.left, root2.left)
        r= self.mergeTwoBinary(root1.right, root2.right)
        root1.left=l
        root2.right= r
        return root1
    def BstToFlatter(self,root):
        """using morrise traversal"""
        curr= root
        while curr is not None:
            if(curr.left is not None):
                if(curr.right is not None):
                    left= curr.left
                    while left.right is not None:
                        left= left.right
                    left.right= curr.right
                curr.right= left.right
                curr.left= None
        curr= curr.right
    def sortedArrayToBST(self,array):
        def dfs(a,start, end):
            if(end>start):
                mid= start+(end-start)//2
                newNode= Node(a[mid])
                newNode.left= dfs(a,start,mid)
                newNode.right= dfs(a,mid+1, end)
                return newNode
        return dfs(a,0,len(array))
    def linkedListToBST(self,head):
        def sortedArray(head):
            path=[]
            curr= head
            while curr is not None:
                path.append(curr.data)
                curr= curr.next
            return path
        def dfs(a,start, end):
            if(start>end):
                return 
            if(end>start):
                mid= start+(end-start)//2
                newNode= Node(a[mid])
                newNode.left= dfs(a, start,mid)
                newNode.right= dfs(a,mid+1,end)
                return newNode
        array= sortedArray(head)
        return dfs(array,0, len(array))


        
        
        
        
            
    


            
                    
