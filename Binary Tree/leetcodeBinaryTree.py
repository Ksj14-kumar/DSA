import sys
class Node:
    def __init__(self,item):
        self.data= item
        self.left= None
        self.right= None

class Pair:
    def __init__(self,root,index) -> None:
        self.node= root
        self.index= index


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

    def ArraySum(self,a,i,sum):
        if(len(a)==i):
            return 
        sum[0] +=a[i]
        self.ArraySum(a,i+1,sum)
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
        if(root1 is None and root2 is None):
            return True
        if(root2 is None or root1 is None):
            return False
        elif(root1.data==root2.data):
            return self.sameTree(root1.left,root2.left) and self.sameTree(root1.right, root2.right)
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
        return dfs(array,0,len(array))
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
    def binaryTreeIntoSortedFlattenTree(self,root):
        dummy= Node(-1)
        pre= dummy
        def inorder(root):
            if(root is None):
                return 
            inorder(root.left)
            self.pre.left= None
            self.pre.right= root
            self.pre= root
            inorder(root.right)

        inorder(root)
        return self.dummy.right
    def searchInBST(self,root,val):
        if(root is None):
            return 
        curr= root
        while curr is not None:
            if(curr.data==val):
                return curr
            elif(curr.data<val):
                curr= curr.right
            else:
                curr= curr.left


        """Medium level questions"""

    def deepestleaveSum(self,root):
        q=[0]
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
            total=[0]
            self.ArraySum(small,0,total)
            ans.append(total[0])
        return ans[len(ans)-1]    
    def insertNodeInBST(self,root,val):
        if(root is None):
            return Node(val)
        if(root.data<val):
            root.right= self.insertNodeInBST(root.right,val)
        else:
            root.left= self.insertNodeInBST(root.left,val)
        return root
    def sumOfNodesWithEvenValuedGrandParent(self,root):
        def dfs(root,p,gp,sum):
            if(root is None):
                return 0
            if(gp is not None and gp.data%2==0):
                sum[0] +=root.data
            dfs(root.left,root,p,sum)
            dfs(root.right,root,p,sum)
        sum=[0]
        dfs(root,None, None,sum)
        return sum[0]

    def averageOfSubtree(self,root):
        def dfs(root,ans):
            if(root is None):
                return (0,0)
            ls,lc= dfs(root.left,ans)
            rs,rc= dfs(root.right,ans)
            sum=ls+rs+root.data
            count = lc+rc+1
            if(sum//count==root.data):
                ans +=1
            return (sum,count)
        ans=[0]
        dfs(root,ans)
        return ans[0]

    def getIndexOfMaxValue(self,a):
        max=a[0]
        count=1
        for i in range(1,len(a)):
            if(max<a[i]):
                count =i
                max=a[i]
        return count

    def MaximumBinaryTree(self,a,start, end):
        if(start>end):
            return
        if(end>start):
            index= start 
            for i in range(start, end):
                index=i if(a[i]>a[index]) else index
            newNode= Node(a[index])
            newNode.left= self.MaximumBinaryTree(a,start,index)
            newNode.right= self.MaximumBinaryTree(a,index+1,end)
            return newNode
    def BalanceBinarySearchTree(self,root):
        def inorder(root,path):
            if(root is None):
                return
            inorder(root.left,path)
            inorder.append(root.data)
            inorder(root.right,path)
            return path

        def createBinaryTree(a,start, end):
            if(start>end):
                return 
            if(end>start):
                mid= start+(end-start)//2
                newNode= Node(a[mid])
                newNode.left= createBinaryTree(a,start,mid)
                newNode.right= createBinaryTree(a,mid+1,end)
                return newNode

        a= inorder(root)
        return createBinaryTree(a,0,len(a))

    def BinarySearchTreeIntoGreaterSum(self,root):
        if(root is None):
            return

    def linkedListInBST(self,root,head):
        def checkLinkedList(root,head):
            if(head is None):
                return True
            if(root is None):
                return False
            if(root.data==head.data):
                return checkLinkedList(root.left,head.next) or checkLinkedList(root.right,head.next)
            return  False
        if(root is None):
            return False
        if(head is None):
            return True
        
        #if if any node element of Linkedlist and BST are same then check further tree side
        isPossible=False
        if(root.data==head.data):
            isPossible= checkLinkedList(root,head)

        #other not match then move tree side left or right
        return isPossible or self.linkedListInBST(root.left, head) or self.linkedListInBST(root.right,head)

    def maximumWidthOfBST(self,root):
        q=[]
        q.append(Pair(root,0)) 
        maxWidth=0
        while len(q)>0:
            size= len(q)
            leftIndex=q[0]
            rightIndex= q[0]
            while size>0:
                rm= q.pop(0)
                node= rm.node
                rightIndex= rm.index
                if(node.left is not None):
                    q.append(Pair(node.left,2*rm.index+1))
                if(node.right is not None):
                    q.append(Pair(node.right,2*rm.index+2))
                size-=1
            maxWidth= max(maxWidth,rightIndex-leftIndex+1)
        return maxWidth

    def longestUniqueValuePath(self,root):
        def uniValueHeight(root,key):
            if(root is None or root.key !=key):
                return 0
            l= uniValueHeight(root.left,key)
            r= uniValueHeight(root.right,key)
            return 1+ max(l,r)
        if(root is None):
            return 0
        l= self.longestUniqueValuePath(root.left)
        r= self.longestUniqueValuePath(root.right)
        sub= max(l,r)
        return max(uniValueHeight(root.left,root.data)+uniValueHeight(root.right,root.data),sub)

    def preOrderSerializationOfBT(self,tree_s):
        if(tree_s is None):
            return False
        # methode-1, using stack
        stack=[]
        for i in stack.split(","):
            curr= i
            while (curr =="#" and len(stack)>0 and stack[-1]==curr):
                stack.pop()
                if(len(stack)==0):
                    return False
                stack.pop()
            stack.append(curr)
        return len(stack)==1 and stack[-1]=="#"

        #methode-2 using diff
        # a= tree_s.split(",")
        # diff=1
        # for i in a:
        #     diff= diff-1
        #     if(diff<0):
        #         return False
        #     if(i !=="#"):
        #         diff +=2
        # return diff==0
    def maximumProductOfSplittedBT(self,root):
        self.ans,self.total=0,0
        def dfs(root):
            if(root is None):
                return 0
            currSum= self.maximumProductOfSplittedBT(root.left)+self.maximumProductOfSplittedBT(root.right)+root.data
            self.ans= max(self.ans,(self.total-currSum)*currSum)
            return currSum
        self.total= dfs(root)
        dfs(root)
        return self.ans%(10**9+7)


    def RecoverBST(self,root):
        """Using Morris traversal, in O(1)"""

        def getRightMost(l,c):
            while l.right is not None and l.right !=c:
                l= l.right
            return l
        curr= root
        while curr is not None:
            left= curr.left
            pre,a,b=None,None,None
            if(left is None):
                if(pre is not None and pre.data>curr.data):
                    if(a is None):
                        a=pre
                    b=curr
                pre=curr
                curr= curr.right
            if(left is not None):
                rightMost= getRightMost(left,curr)
                if(rightMost.right is None):
                    rightMost.right=curr
                    curr=curr.left

                else:
                    rightMost.right=None
                    if(pre.data>curr.data):
                        if(a is None):
                            a=pre
                        b=curr
                    pre=curr
                    curr=curr.right
        if(a is not None):
            a.val,b.val=b.val,a.val
        return root

    def BSTFromPreOrderAndInorder(self,inorder,preorder):
        def dfs(inorder,preOrder,pre_start,pre_end,in_start,in_end):
            if(in_start>in_end):
                return
            index= pre_start
            while inorder[index]>pre_start[pre_start]:
                index+=1
            lrange= index=in_start
            newNode= Node(preOrder[pre_start])
            newNode.left=dfs(inorder,preOrder,pre_start+1,pre_start+lrange,in_start,index-1)
            newNode.right=dfs(inorder,pre_end,pre_start+lrange+1,index-1,in_end)
            return newNode
        return dfs(inorder,preorder,0,len(preorder)-1,0,len(inorder))
        

    def BSTFromInorderAndPostOrder(self,inorder,postorder):
        def dfs(inorder,postorder,in_start,in_end,post_start,post_end):
            if(in_start>in_end):
                return
            index=in_start
            while inorder[index] !=postorder[post_end]:
                index +=1
            lrange= index-in_start
            newNode= Node(postorder[post_end])
            newNode.left= dfs(inorder,postorder,in_start,index-1,post_start,post_start+lrange-1)
            newNode.right= dfs(inorder,postorder,index-1,in_end,post_start+lrange,post_end-1)
            return newNode
    def maximumPathSum(self,root,result=-sys.maxsize):

        if(root is None):
            return 0,result
        left,result= self.maximumPathSum(root.left,result)
        right, result= self.maximumPathSum(root.right, result)
        result= max(result,root.val)
        result= max(result,root.val+left)
        result= max(result,root.right+right)
        result= max(result,root.val+left+right)
        return max(root.val,max(left,right)+root.val),result
    def sumofLeftLeaves(self,root):
        def dfs(root,isLeft=False):
            if(root is None):
                return 0
            if(root.left is None and root.right is None):
                return root.data if isLeft else 0
            l= dfs(root.left,True)
            r= dfs(root.right,False)
            return l+r
        return dfs(root)

    def modeInBinaryTree(self,root):
        """ TC=O(n),SC=(n)"""
        def mode(root,d):
            if(root is None):
                return
            d[root.val]=d.get(root.val,0)+1
            mode(root.left,d)
            mode(root.right,d)
        d={}
        mode(root,d)
        max_count= max(d.values())
        return [i for i in d if d[i]==max_count]
    def frequentlySubtree(self,root):
        """ TC=O(n),SC=(n)"""
        def dfs(root,d):
            if(root is None):
                return
            l= dfs(root.left,d)
            r= dfs(root.right,d)
            total=l+r+root.val
            d[total]=d.get(total,0)+1
            return total
        d={}
        dfs(root,d)
        max_count=max(d.values())
        return [i for i in d if d[i]==max_count]

    def twoNodeExitInTreeWhoseSumEqual(self,root,k):
        def dfs(root,path):
            if(root is None):
                return 
            dfs(root.left,path)
            path.append(root.val)
            dfs(root.right,path)
        path=[]
        dfs(root,path)
        start=0
        end=len(start)-1
        while end>start:
            if(path[start]+path[end]==k):
                return True
            elif(path[start]+path[end]<k):
                start +=1
            else:
                end -=1
        return False
    def minimumAbsoluteDifference(self,root):
        def dfs(root,path):
            if(root is None):
                return 
            dfs(root.left,path)
            path.append(root.val)
            dfs(root.right,path)
            
        path=[]
        dfs(root,path)
        min_value=sys.maxsize
        for u in range(len(path)-1):
            if(path[u+1]-path[u]<min_value):
                min_value=path[u+1]-path[u]
        return min_value
    def addNewRowIntotree(self,root,depth,val):
        def helper(root,d,val):
            if(root is None):
                return 
            if(d==2):
                left= root.left
                right= root.right
                newNodeLeft=Node(val)
                newNodeRight= Node(val)
                newNodeLeft.left= left
                newNodeLeft.right=right
                root.left=newNodeLeft
                root.right=newNodeRight
            helper(root.left,d-1,val)
            helper(root.right,d-1,val)
        def dfs(root,depth,val):
            if(depth==1):
                newNode=Node(val)
                newNode.left=root
                return newNode

            helper(root,depth,val)
            return root


             
            


        




        

        


        

    







b= BinaryTree()

# print(b.PreOrderTraversal(b.MaximumBinaryTree([3,2,1,6,0,5])))


print(all([True,True,False]))

                

        
            


        
        
        
        
            
    


            
                    
