import sys
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class Pair:
    def __init__(self,root,index) -> None:
        self.node= root
        self.index=index

class BSTIterator:
    def __init__(self,root) -> None:
        self.curr=root

    def next(self):
        value = self.morrisTraversal()
        return value.data

    def hasNext(self):
        return self.curr is not None

    def morrisTraversal(self):
        res=None
        while self.curr is not None:
            left= self.curr.left
            if(left is None):
                res= self.curr
                self.curr= self.curr.right
                break
            else:
                rightMost= self.getRightMost(left,self.curr)
                if(rightMost.right is None):
                    rightMost.right= self.curr
                    self.curr= self.curr.left
                else:
                    res= self.curr
                    rightMost.right= None
                    self.curr= self.curr.right
                    break
        return res


    def getRightMost(self,l,c):
        while l.right is not None and l.right !=c:
            l=l.right
        return l








class BinaryTree:
    def inorderTraversal(self,root):
        def dfs(root,path):
            if(root is None):
                return 
            dfs(root.left,path)
            path.append(root.data)
            dfs(root.right,path)
            return path
        path=[]
        dfs(root,path)
        return path

    def NumberofUniqueBST(self,n):
        def fact(n):
            f=1
            for i in range(2,n+1):
                f *=i
            return f
        upper= fact(2*n)
        lower= fact(n+1)*fact(n)
        return (upper//lower)%(10**9+7)

    def UniqueBSTs(self,n):
        def dfs(start,end):
            array=[]
            if(start>end):
                array.append(None)
                return array
            
            for i in range(start,end+1):
                leftTreeArray= dfs(start,i-1)
                rightTreeArray= dfs(i+1,end)
                for l in leftTreeArray:
                    for r in rightTreeArray:
                        newNode= Node(i)
                        newNode.left=l
                        newNode.right=r
                        array.append(newNode)
            return array
        return dfs(1,n)

    def balancedBST(self,root):
        def getHeight(root):
            if(root is None):
                return 0
            l= getHeight(root.left)
            r= getHeight(root.right)
            if(l==-1):
                return -1
            if(r==-1):
                return -1
            if(abs(l-r)>1):
                return -1
            return max(l,r)+1
        def dfs(root):

            if(root is None):
                return True
            if(getHeight(root)==-1):
                return False
            return True
        return dfs(root)

    def minDepth(self,root):
        def dfs(root):
            if(root is None):
                return 0
            l= dfs(root.left)
            r= dfs(root.right)
            if(l==0):
                return r+1
            if(r==0):
                return l+1
            return min(l,r)+1
        return dfs(root)
    def binaryTreeIntoSkewRightTree(self,root):
        def dfs(root):
            curr= root
            while curr is not None:
                left= curr.left
                right= curr.right
                curr.left=None
                curr.right=None
                curr.right=left
                temp=curr
                while temp.right is  not None:
                    temp=temp.right
                temp.right=right
                curr=curr.right
            return root
        return dfs(root)

    def sortedArrayTOBST(self,a):
        def dfs(a,start,end):
            if(end>start):
                mid= start+(end-start)//2
                newNode= Node(a[mid])
                newNode.left=dfs(a,start,mid)
                newNode.right=dfs(a,mid+1,end)
                return newNode

        print(self.inorderTraversal(dfs(a,0,len(a))))
        return dfs(a,0,len(a))

    def ConvertLinkedListToBT(self,head):
        def methode_1(head):
            def createTree(a,start,end):
                if(end>start):
                    mid= start+(end-start)//2
                    newNode= Node(a[mid])
                    newNode.left= createTree(a,start,mid)
                    newNode.right= createTree(a,mid+1,end)
                    return newNode
            if(head is None):
                return 
            a=[]
            curr= head
            while curr is not None:
                a.append(curr.data)
                curr= curr.next
            return createTree(a,0,len(a))

        def methode_2(head):

            if(head is None):
                return head
            if(head.next is None):
                return Node(head.val)
            pre,slow,fast=None,head,head
            while fast is not None and fast.next is not None:
                pre=slow
                slow= slow.next
                fast= fast.next.next
            pre.next=None # break linked list into two parts
            newNode= Node(slow.data)
            newNode.left= methode_2(head)
            newNode.right= methode_2(slow.next)
            return newNode
    def levelOrderTraversal(self,root):
        q=[]
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
                size-=1
            ans.extend(small)
        return ans

    def sameTree(self,r1,r2):
        if(r1 is  None and r2 is  None):
            return True
        if(r1 is None or r2 is None):
            return False
        if(r1.data==r2.data):
            return self.sameTree(r1.left,r2.left) and self.sameTree(r1.right, r2.right)
        return False
    def symmetricTree(self,root):
        if(root is None):
            return True
        def dfs(r1, r2):
            if(r1 is None and r2 is None):
                return True
            if(r1 is None or r2 is None):
                return False
            if(r1.data ==r2.data):
                return dfs(r1.left,r2.right) and dfs(r1.right, r2.left)
            return False
        return dfs(root.left,root.right)

    def recoverBinaryTree(self,root):
        def getRightMost(l,c):
            while l.right is not None and l.right !=c:
                l=l.right
            return l

        curr= root
        pre,a,b=None,None,None
        while curr is not None:
            left= curr.left
            if(left is None):
                if(pre is not None and pre.data>curr.data):
                    if(a is None):
                        a= pre
                    b= curr
                pre=curr
                curr= curr.right
            if(left is not None):
                rightMost= getRightMost(left,curr)
                if(rightMost.right is None):
                    rightMost.right= curr
                    curr= curr.left
                else:
                    rightMost.right=None
                    if(pre is not None and pre.data>curr.data):
                        if(a is None):
                            a=pre
                        b=curr
                    pre=curr
                    curr= curr.right

        if(a is not None):
            a.data,b.data= b.data,a.data
        return root


    def populatenextRightPointer(self,root):
        def dfs(root):
            q=[]
            q.append(root)
            while len(q)>0:
                size= len(q)
                small=[]
                while size>0:
                    rm =q.pop(0)
                    small.append(rm)
                    if(rm.left is not None):
                        q.append(rm.left)
                    if(rm.rigth is not None):
                        q.append(rm.right)
                    size-=1
                for i in range(len(small)-1):
                    small[i].next= small[i+1]
            return root
        return dfs(root)
    def maximumPathSum(self,root):
        def dfs(root,res=-sys.maxsize):
            if(root is None):
                return 0,res
            l= dfs(root.left, res)
            r= dfs(root.right, res)
            res= max(res,root.val)
            res= max(res,l+root.val)
            res= max(res, r+root.val)
            res= max(res,l+r+root.val)
            return max(root.val,max(l,r)+root.val), res
        return dfs(root)[1]

    def sizeOfTree(self,root):
        if(root is None):
            return 0
        l= self.sizeOfTree(root.left)
        r= self.sizeOfTree(root.right)
        return l+1+r

    def binaryTreeInvert(self,root):
        def dfs(root):
            if(root is None):
                return 
            dfs(root.left)
            dfs(root.right)
            root.left,root.right= root.right,root.left
            return root
        return dfs(root)

    def ktSmallestElementInBST(self,root,k):
        def dfs(root,path):
            if(root is None):
                return 
            dfs(root.left,path)
            if(root.val not in path):
                path.append(root.data)
            dfs(root.right,path)
        path=[]
        dfs(root,path)
        return path[k-1]
    def BinaryTreePathAsString(self,root):
        def dfs(root,s,path,paths):
            if(root is None):
                return 
            s +=f"{root.data}->" if(root.left is not None or root.right is not None) else f"{root.data}"
            path.append(s)
            if(root.left is None and root.right is None):
                paths.append(path[-1])
            dfs(root.left,s,path,paths)
            dfs(root.right,s,path,paths)

        path,paths=[],[]
        dfs(root,"",path,paths)
        return paths

    def serializedOfTree(self,root):
        def dfs(root,a):
            if(root is None):
                a.append("null")
                return 
            a.append(f"{root.data}")
            dfs(root.left,a)
            dfs(root.right,a)
        a=[]
        dfs(root,a)
        return ",".join(a)
    def deserilizedOfTree(self,s):
        self.i=0
        def dfs(a):
            if(len(a)==self.i or a[self.i]=="null"):
                self.i+=1
                return 
            newNode= Node(int(a[self.i]))
            self.i +=1
            newNode.left= dfs(a)
            newNode.right =dfs(a)
            return newNode
        b=s.split(",")
        return dfs(b)
    def preorderSerializationOfBST(self,s):
        a= s.split(",")
        stack=[]
        for i in a:
            curr= i
            while len(stack)>0 and stack[-1]==curr and curr=="#":
                stack.pop()
                if(len(stack)==0):
                    return False
                stack.pop()
            stack.append(curr)
        return len(stack)==1 and stack[-1]=="#"

    def sumOfLeftLeaves(self,root):
        def dfs(root,b,total):
            if(root is None):
                return 0
            
            if(root.left is None and root.right is None):
                total[0]+= root.val if b else 0
            dfs(root.left,True,total)
            dfs(root.right,False,total)
        total=[0]
        return dfs(root,False,total)

    def deleteNode(self,root,key):
        def getMinValue(root):
            if(root is None or root.left is None):
                return root
            return getMinValue(root.left)
        def dfs(root,key):
            if(root is None):
                return
            if(root.data<key):
                root.right= dfs(root.right,key)
            elif(root.data>key):
                root.left= dfs(root.left,key)
            else:
                if(root.left is None):
                    right= root.right
                    root= None
                    return right
                elif(root.right is None):
                    left=root.left
                    root= None
                    return left
                else:
                    temp= getMinValue(root.right)
                    root.data=temp.data
                    root.right= dfs(root.right,temp.data)
            return root
        return dfs(root,key)

    def modeOfBT(self,root):
        def mode(root,d):
            if(root is None):
                return 
            d[root.data]= d.get(root.data,0)+1
            mode(root.left,d)
            mode(root.right,d)

        d={}
        mode(root,d)
        maxValue= max(d.values())
        # print(d)
        l=[]
        for i in d:
            if(d[i]==maxValue):
                l.append(i)
        return l
    def frequentlySubTreeSum(self,root):
        def dfs(root,d):
            if(root is None):
                return 0
            l= dfs(root.left,d)
            r= dfs(root.right,d)
            total= root.val+l+r
            d[total]=d.get(total,0)+1
            return total
        d= {}
        dfs(root,d)
        maxCount = max(d.values())
        return [key for key in d if d[key]==maxCount]

    def findBottomLeftTreeValue(self,root):
        "level order traversal"
        q=[]
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
                size-=1
            ans.append(small)
        return ans[-1][0]

    def getMinimumDifferenceInBST(self,root):
        def dfs(root,path):
            if(root is None):
                return 
            dfs(root.left,path)
            path.append(root.data)
            dfs(root.right,path)
            return path
        path=[]
        dfs(root,path)
        print(path)
        # get min difference in sorted array
        minValue= float("inf")
        for i in range(len(path)-1):
            if(path[i+1]-path[i]<minValue):
                minValue=path[i+1]-path[i]
        return minValue

    def bstToGreaterSum(self,root):
        self.t=0
        def dfs(root):
            if(root is None):
                return 0
            dfs(root.left)
            self.t+=root.data
            root.val= self.t
            dfs(root.right)
            return root
        return dfs(root)

    def height(self,root):
        if(root is None):
            return 0
        l= self.height(root.left)
        r= self.height(root.right)
        return max(l,r)+1
            
    def diameterOfTree(self,root):
        if(root is None):
            return 0
        d1= self.diameterOfTree(root.left)
        d2= self.diameterOfTree(root.right)
        l= self.height(root.left)
        r= self.height(root.right)
        total=l+r+2
        return max(total,max(d1,d2))


    def tiltOfBinaryTree(self,root):
        def dfs(root,tilt):
            if(root is None):
                return 0
            l= dfs(root.left,tilt)
            r= dfs(root.right,tilt)
            tilt[0]+= abs(l-r)
            return root.val+l+r
        titl=[0]
        dfs(root,titl)
        return titl[0]

    def stringFromBinaryTree(self,root):
        def dfs(root,s=""):
            if(root is None):
                return ""
            s= str(root.data)
            if(root.left is not None):
                s+="("+str(dfs(root.left, s))+")"
            if(root.right is not None):
                if(root.left is None):
                    s+="()"
                s+="("+str(dfs(root.right,s))+")"
            return s
        return dfs(root)
    def mergeBT(self,r1,r2):
        def dfs(r1,r2):
            if(r1 is None):
                return r2
            if(r2 is None):
                return r1
            r1.data+=r2.data
            l= dfs(r1.left,r2.left)
            r= dfs(r1.right, r2.right)
            r1.left= l
            r1.right=r
            return r1
        return dfs(r1,r2)
    
    def createTreeMaxiMumBinaryTree(self,a):
        def to_tree(a,start,end):
            if(start>=end):
                return 
            index= start
            for i in range(start,end):
                index= i if(a[i]>[index]) else index
                newNode= Node(a[i])
                newNode.left= to_tree(a,start,index)
                newNode.right= to_tree(a,index+1,end)
                return newNode
        return to_tree(a,0,len(a))

    def addrowIntoTree(self,root,d,val):
        def addRow(root,d,val):
            if(root is None):
                return 

            if(d==2):
                left= root.left
                right= root.right
                newNodeLeft=Node(val)
                newNodeRight= Node(val)
                newNodeLeft.left= left
                newNodeLeft.right= right
                root.left= newNodeLeft
                root.right= newNodeRight
            else:
                addRow(root.left,d-1,val)
                addRow(root.right,d-1,val)
            return root
        def dfs(root,d,val):
            if(d==1):
                newNode= Node(val)
                newNode.right= root
                return newNode
            addRow(root,d,val)
            return root
        return dfs(root,d,val)

    def maximumWidth(self,root):
        "width of tree"
        q=[]
        maxValue=float("-inf")
        q.append(Pair(root,0))
        while len(q)>0:
            size =len(q)
            leftIndex= q[0].index
            rightIndex= q[0].index
            while size>0:
                rm= q.pop(0)
                i= rm.index
                node= rm.node
                rightIndex=i
                if(node.left is not None):
                    q.append(Pair(node.left,2*i+1))
                if(node.right is not None):
                    q.append(Pair(node.right,2*i+2))
                size-=1
            maxValue= max(maxValue,rightIndex-leftIndex+1)
        return maxValue
    def longestUniqueValuePath(self,root):
        def getUnique(root,key):
            if(root is None or root.data !=key):
                return 0
            l= getUnique(root.left,key)
            r= getUnique(root.right,key)
            return max(l,r)+1
        def dfs(root):
            if(root is None):
                return 0

            l= dfs(root.left)
            r= dfs(root.right)
            sub= max(l,r)
            lh= getUnique(root.left,root.val)
            rh= getUnique(root.right,root.val)
            return max(lh+rh,sub)
        return dfs(root)

    def BinaryTreePruning(self,root):
        def prune(root):
            if(root is None):
                return False

            l= prune(root.left)
            r= prune(root.right)
            if(not l):
                root.left=None
            if(not r):
                root.right=None
            return root.val==1 or l or r

        def dfs(root):
            if(not prune(root)):
                return None
            return root
        return dfs(root)
    def searchValueInBST(self,root,key):
        def dfs(root,key):
            if(root is None):
                return 
            if(root.data==key):
                return root
            if(root.data<key):
                return dfs(root.right,key)
            if(root.key>key):
                return dfs(root.left,key)
        return dfs(root,key)
    def insertIntoBST(self,root,data):
        def dfs(root,data):
            if(root is None):
                return Node(data)
            if(root.data>data):
                root.right= dfs(root.right,data)
            if(root.data<data):
                root.left= dfs(root.left,data)
            return root
        return dfs(root,data)

    def CountNodesEqualtoAverageofSubtree(self,root):
        def dfs(root,ans):
            if(root is None):
                return 0,0
            lc,ls= dfs(root.left,ans)
            rc,rs= dfs(root.right,ans)
            total= ls+rs+root.data
            count= lc+rc+1
            if(total//count==root.val):
                ans[0]+=1
            return (total,count)
        ans=[0]
        dfs(root,ans)
        return ans[0]

    def AllAboutTree(self,root):
        def dfs(root):
            if(root is None):
                return (0,0,0)
            ls,lc,lh= dfs(root.left)
            rs,rc,rh= dfs(root.right)
            total= ls+rs+root.data
            count = lc+rc+1
            height=max(lh,rh)+1
            return (total,count,height)
        return dfs(root)

    def k_levelDownFromRoot(self,root,k):
        def dfs(root,k,ans):
            if(root is None or k<0):
                return 
            if(k==0):
                ans.append(root.data)
                return 
            dfs(root.left,k-1,ans)
            dfs(root.rigth,k-1,ans)
        ans=[]
        dfs(root,k,ans)
        return ans
    def k_level_down_from_node(self,root,target,k):
        def dfs(root,target,l,ans):
            if(root is None):
                return 
            if(root.data==target):
                ans.extend(self.k_levelDownFromRoot(root,l))
                return 
            dfs(root.left,target,l,ans)
            dfs(root.right,target,l,ans)
        ans=[]
        dfs(root,target,k,ans)
        return ans

    def reverOddLevelOfTree(self,root):
        def dfs(r1,r2,level):
            if(r1 is None or r2 is None):
                return
            if(level):
                r1.data,r2.data= r1.data,r2.data
            dfs(r1.left,r2.right,not level)
            dfs(r1.right,r2.left,not level)
        dfs(root.left,root.right,True)
        return root
    def ReverEvenLevel(self,root):
        def dfs(r1,r2,level):
            if(r1 is None or r2 is None):
                return 
            if(level):
                r1.val,r2.val= r2.val,r1.val
            dfs(r1.left,r2.right,not level)
            dfs(r1.right,r2.left,not level)
        dfs(root.left,root.right,False)
        return root
    def delete_node(self,root, to_delete):
        def dfs(root, from_delete):
            if(not root):
                return 
            root.left= dfs(root.left,from_delete)
            root.right= dfs(root.right, from_delete)
            if(root.val in from_delete):
                if(root.left is not None):
                    output.append(root.left)
                if(root.right is not None):
                    output.append(root.right)
                return 
            return root
        to_delete_set= set(to_delete)
        output=[]
        if(root.val in to_delete_set):
            output.append(root)
        dfs(root,to_delete_set)
        return output
    def FlipEquivalentBinaryTrees(self,r1,r2):
        def dfs(r1,r2):
            if(r1 is None and r2 is None):
                return True
            if(r1 is None or r1 is None):
                return False
            if(r1.data !=r2.data):
                return False
            l= dfs(r1.left,r2.left) and dfs(r1.right, r2.right)
            r=dfs(r1.left, r2.right) and dfs(r1.right, r2.left)
            return l or r
        return dfs(r1,r2)

    def trimOfBST(self,root,low,high):
        def dfs(root,l,u):
            if(root is None):
                return
            root.left=dfs(root.left,l,u)
            root.right= dfs(root.right,l,u)
            if(root.val>u):
                return dfs(root.left,l,u)
            if(root.val<l):
                return dfs(root.right,l,u)
            
            return root
        return dfs(root,low,high)
    def psuedoPalindromicPath(self,root):
        def dfs(root,count):
            if(root is None):
                return 0
            count =count^(1<<root.data)
            l= dfs(root.left,count)
            r= dfs(root.right,count)
            res= l+r
            if(root.left==root.right):
                if(count & count-1==0):
                    res +=1
            return res
        return dfs(root,0)
    def isSame(self,r1,r2):
        if(r1 is None and r2 is None):
            return True
        if(r1 is None or r2 is None):
            return False
        if(r1.data==r2.data):
            return self.isSame(r1.left,r2.left) and self.isSame(r1.right, r2.right)
        return False

    def subtree_of_another_tree(self,root,sub):
        def dfs(root,sub):
            if(root is None):
                return False
            if(self.isSame(root,sub)):
                return True
            l= dfs(root.left,sub)
            r= dfs(root.right,sub)
            return l or r

        return dfs(root,sub)
            






                

    




            
                

           


    
            




            


        
        

        



            



    


                
                



            
    

            
            
            
            
                        
                

                            






b= BinaryTree()
n1= Node(1)
n2= Node(2)
n3= Node(3)
n4= Node(4)
n5= Node(5)
n6= Node(6)
n7= Node(7)
n8= Node(8)
n9= Node(9)
n10= Node(10)
n11= Node(11)
n12= Node(12)
n13= Node(13)
tree = Node(0)
tree.left= n1
tree.right= n2
n1.left=n3
n1.right= n4
n2.left=n5
n2.right=n6
n3.left=n7
n3.right=n8
n4.left=n5
n5.left=n6
n5.right=n13
n6.left=n7
n7.left=n8



# b.NumberofUniqueBST(887)
# print(b.UniqueBSTs(5))
# print(b.balancedBST(tree))
# b.binaryTreeIntoSkewRightTree(tree)
# b.sortedArrayTOBST([1,2,3,4,5,6,7])
# print(b.BinaryTreePathAsString(tree))
# print(b.serializedOfTree(tree))
# print(tree==)
# print(b.inorderTraversal(b.deserilizedOfTree(b.serializedOfTree(tree))))
# print(b.inorderTraversal(tree))
# b.modeOfBT(tree)
# print(b.findBottomLeftTreeValue(tree))
# print(b.bstToGreaterSum(tree))
# print(b.diameterOfTree(tree))
# print(b.stringFromBinaryTree(tree))
# print(b.AllAboutTree(tree))












d={}
for i in [1,3,2,5]:
    d[i]= d.get(i,0)+1





# def fact(n,callStack):
#     # this method work only for [0-997]
#     callStack.append(n)
#     print(callStack)
#     if(n==0):
#         callStack.pop()
#         print(callStack)
#         return 1
#     value= n*fact(n-1,callStack)
#     callStack.pop()
#     print(callStack)
#     return value
# callStack=[]
# # print(fact(8,callStack))


# def fact1(n): 
#     # factorial of a large number using bigInt, Tc=O(n)
#     f=1
#     for i in range(2,n+1):
#         f*=i
#     return f

# # print(fact1(1010))            
