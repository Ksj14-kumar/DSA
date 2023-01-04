import sys
from tkinter import X
# ternnary operator i python
# do1 if statement else do2
def maximum(v1, v2):
    return v1 if v1>v2 else v2
# minimum
def minimum(v1, v2):
    return v2 if v1>v2 else v1
class Node:
    def __init__(self, item) -> None:
        self.left= None
        self.right= None
        self.data= item
class Pairs:
    def __init__(self,Node, state) -> None:
        self.node= Node
        self.state= state
class Tree:
    def __init__(self) -> None:
        self.call= ""
        self.returned=None
        self.childrens=[]

# minimum and second minimum element
a=[12, 13, 1, 10, 34, 1,1,10]
minimum=sys.maxsize
for i in a:
    if(i<minimum):
        minimum=i
print(minimum)
second= sys.maxsize
for i in a:
    if(i<second and i>minimum):
        second=i
print(second)





def printTree(tree, indent=""):
    size= 4
    if(tree is None or len(tree.childrens)==0):
        print(tree.call+" returned "+str(tree.returned))
    else:
        print(tree.call+" returned "+str(tree.returned))
        for child in tree.childrens[:-1]:
            print(indent+"|"+"-"*size,end=" ")
            printTree(child, indent+"|"+"-"*size)
        child=tree.childrens[:-1]
        print(indent+"L"+"-"*size)
        printTree(child,indent+" "*size)

    

def maximum(n1,n2):
    return n1 if n1>n2 else n2

class BinaryTree:
    def __init__(self) -> None:
        self.stack=[]
        self.pre_start=0

    def createTree(self,array):
        root_node= Node(array[0])
        root_pair= Pairs(root_node,1)
        self.stack.append(root_pair)
        index= 0
        while len(self.stack)>0:
            top= self.stack[-1]
            # index +=1
            if(top.state==1):
                index +=1
                if(array[index] is not None):

                    newNode= Node(array[index])
                    top.node.left= newNode
                    top.state +=1
                    left_pair= Pairs(newNode,1)
                    self.stack.append(left_pair)
                else:
                    top.node.left= None
                    top.state +=1
            elif(top.state==2):
                index +=1
                if(array[index] is not None):

                    newNode_right= Node(array[index])
                    top.node.right= newNode_right
                    top.state +=1
                    right_pair= Pairs(newNode_right,1)
                    self.stack.append(right_pair)
                else:
                    top.node.right= None
                    top.state +=1
            else:
                self.stack.pop()
        return root_node
     

    def size_of_binary_tree(self, root):
        if(root is None):
            return 0
        left_size= self.size_of_binary_tree(root.left)
        right_size= self.size_of_binary_tree(root.right)
        return left_size+right_size+1

    def Sum_of_tree(self,root):
        if(root is None):
            return 0
        left_sum= self.Sum_of_tree(root.left)
        right_sum= self.Sum_of_tree(root.right)
        return left_sum+right_sum+root.data
    def height(self, root):
        if(root is None):
            return 0
        left_height= self.height(root.left)
        right_height= self.height(root.right)
        return maximum(left_height,right_height)+1
    def maximum_value(self,root,callStack):
        callStack.append(f"value {root}")
        print(callStack)
        if(root is None):
            callStack.pop()
            print(callStack)
            return -math.inf
        left_side= self.maximum_value(root.left,callStack)
        right_side= self.maximum_value(root.right,callStack)
        value= maximum(maximum(left_side,right_side),root.data)
        callStack.pop()
        print(callStack)
        return value
    def min_value(self, root):
        if(root is None):
            return math.inf
        left_side= self.min_value(root.left)
        right_side= self.min_value(root.right)
        return minimum(minimum(left_side,right_side),root.data)
    def traversal(self,root):
        if(root is None):
            return 
        print("pre", root.data)
        self.traversal(root.left)
        print("In", root.data)
        self.traversal(root.right)
        print("Post",root.data)
    def insertANode(self,root,nodeValue,data):
        if(root is None):
            return
        left= self.insertANode(root.left,nodeValue,data)
        right=self.insertANode(root.right,nodeValue,data)
        newNode= Node(data)
        if(root.data==nodeValue):
            root.left=newNode
            newNode.left=left
            newNode.right=right

        return root
    def minDepth(self,root, tree):
        tree.call= f"changeable {root}"
        if(root is None):
            tree.returned= 0
            return 0
        
        child= Tree()
        tree.childrens.append(child)
        left= self.minDepth(root.left,child)
        child= Tree()
        tree.childrens.append(child)
        right= self.minDepth(root.right,child)
        if(left ==0):
            tree.returned= 1+right
            return 1+right
        elif(right==0):
            tree.returned= 1+left
            return 1+left
        else:
            tree.returned= min(left, right)+1
            return min(left, right)+1
    def isBalanced(self,root):
        if(root is None):
            return True
        left= self.isBalanced(root.left)
        right= self.isBalanced(root.right)
        if(left==-1):
            return -1
        if(right==-1):
            return -1
        if(abs(left-right)>1):
            return -1
        return max(left, right)+1
    def paths(self,root):
        def dfs(root,s,path,paths):
            if(root is None):
                return 
            path.append(root.data)
            print("path",path)
            if(root.left is None and root.right is None):
                paths.append(path.copy())
                # print("paths ",paths)
            dfs(root.left,s,path,paths)
            dfs(root.right,s,path,paths)
            path.pop()
            print("path",path)
            return paths
        path=[]
        paths=[]
        s=""
        dfs(root, s,path,paths)
        return paths
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
    def symmetric(self,root,callStack):
        if(root is None):
            return True
        def dfs(root1, root2,callStack):
            callStack.append((root1.data,root2.data))
            print(callStack)
            print((root1.data,root2.data))
            if(root1 is None and root2 is None):
                callStack.pop()
                print(callStack)
                return True
            if(root1 is None or root2 is None):
                callStack.pop()
                print(callStack)
                return False
            if(root1.data==root2.data):
                value =dfs(root1.left, root2.right,callStack) and dfs(root1.right, root2.left,callStack)
                callStack.pop()
                print(callStack)
                return value
        return dfs(root.left, root.right,callStack)
    def binaryTreeCallStack(self,root,callStack):
        callStack.append(root)
        print(callStack)
        if(root is None):
            callStack.pop()
            print(callStack)
            return
            
        self.binaryTreeCallStack(root.left,callStack)
        self.binaryTreeCallStack(root.right,callStack)
        callStack.pop()
        print(callStack)
        return
    def nodeToRootPath(self, root,value):
        def dfs(root):
            if(root is None):
                return False
            if(root.data==value):
                return True
            left= dfs(root.left)
            if(left):
                return True
            right= dfs(root.right)
            if(right):
                return True
            return False
        return dfs(root)
    def searchElementInTree(self,root,value,path,paths):
        if(root is None):
            return False
        path.append(root.data)
        if(self.searchElementInTree(root.left,value,path,paths) or root.data==value  or self.searchElementInTree(root.right, value,path,paths)):
            paths.append(path.copy())
            return True
        path.pop()
        return False
    def fact(self,n):
        if(n<=1):
            return 0
        return self.fact(n-1) or self.fact(n-2)
    def kthLevelDown(self,root, k):
        if(root is None or k<0):
            return 
        if(k==0):
            print(root.data, end=" ")
        self.kthLevelDown(root.left,k-1)
        self.kthLevelDown(root.right,k-1)
    def pathLeaveToRoot(self, root,path, paths,sum):
        if(root is None):
            return 
        sum +=root.data
        path.append(root.data)
        if(root.left is None and root.right is None):
            paths.append(path.copy())
        self.pathLeaveToRoot(root.left,path,paths,sum)
        self.pathLeaveToRoot(root.right,path,paths,sum)
        path.pop()
        return 
    def leftClonedTree(self, root):
        if(root is None):
            return
        left= self.leftClonedTree(root.left)
        right= self.leftClonedTree(root.right)
        newNode= Node(root.data)
        newNode.left= left
        root.left= newNode
        root.right=right
        return root
    def insertionLeft(self,root,d):
        if(root is None):
            return False
        
        left= self.insertionLeft(root.left,d)
        right= self.insertionLeft(root.right,d)
        if(root.data==d or left or right):
            newNode= Node(100)
            newNode.left= left
            root.left=newNode
            root.right= right
            return True
        return False
    def pathOfNode(self, root,value,path,paths):
        if(root is None):
            return
        path.append(root.data)
        value= root.data==value or self.pathOfNode(root.left,value,path,paths) or self.pathOfNode(root.right,value,path,paths)
        if(value):
            paths.append(path.copy())
        path.pop()
        return paths
    def levelOfNode(self,root,x,count):
        if(root is None):
            return 0
        if(root.data==x):
            return count
        value= self.levelOfNode(root.left,x,count+1)
        if(value !=0):
            return count
        return self.levelOfNode(root.right,x,count+1)
    def isCousins(self,root,x,y):
        paths=[]
        path=[]
        levelX=self.pathOfNode(root,x,path,paths)
        ps1=[]
        p1=[]
        levelY= self.pathOfNode(root,y,ps1,p1)
        if(len(levelX)==len(levelY)):
            def dfs(root,x,y):

                if(root is None):
                    return 0
                return (root.left==x and root.right==y) or (root.left==y and root.right==x) or dfs(root.left,x,y) or dfs(root.right,x,y)
            return dfs(root,x,y)
        return False
    def binaryTreeToFlatten(self,root):
        "Binary tree into flatten tree in any order"
        if(root is None):
            return root
        curr= root
        while curr is not None:
            if(curr.left is not None):
                if(curr.right is not None):
                    l= curr.left
                    while l.right is not None:
                        l= l.right
                    l.right= curr.right
                curr.right= curr.left
                curr.left=None
            curr= curr.right
        return root
    def BinaryTreeIntoSortedFlatten(self,root):
        dummy= Node(-1)
        pre= dummy
        def inorderTraversal(root):
            if(root is None):
                return
            inorderTraversal(root.left)
            self.pre.left= None
            self.pre.right= root
            self.pre= root
            inorderTraversal(root.right)
        inorderTraversal(root)
        return self.dummy.right
            

        
    def leftView(self,root):
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
                size -=1
        ans.append(small[0])
    def verticalOrderTraversal(self,root):
        q=[]
        ans=[2,2]
        self.widthOfBinaryTree(root,0,ans)
        w= ans[1]-ans[0]+1
        answer=[]
        for _ in range(w):
            answer.append([])
        q.append(Pairs(root,abs(ans[0])))
        
        while len(q)>0:
            size= len(q)
            while size>0:
                rm=q.pop(0)
                node= rm.node
                hl= rm.state
                answer[hl].append(node.data)
                if(node.left is not None):
                    q.append(Pairs(node.left,hl-1))
                if(node.right is not None):
                    q.append(Pairs(node.right,hl+1))
                size -=1
        return answer
    def widthOfBinaryTree(self,root,hl,ans):
        if(root is None):
            return 
        ans[0]= min(ans[0],hl)
        ans[1]= max(ans[1],hl)
        self.widthOfBinaryTree(root.left, hl-1,ans)
        self.widthOfBinaryTree(root.right, hl+1,ans)
    def levelOrderTraversal(self,root):
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
    
    def SortedArrayToBinaryTree(self,a,start, end):
        if(end>start):
            mid= start+(end-start)//2
            newNode= Node(a[mid])
            left= self.SortedArrayToBinaryTree(a, start,mid)
            right= self.SortedArrayToBinaryTree(a,mid+1,end)
            newNode.left= left
            newNode.right= right
            return newNode
    def linkedListToBST(self,head):
        def sortedArray(head):
            curr= head
            path= []
            while curr is not None:
                path.append(curr.data)
                curr= curr.next
            return path
        def dfs(a,start,end):
            if(start>end):
                return
            if(end>start):
                mid= start+(end-start)//2
                newNode= Node(a[mid])
                newNode.left= dfs(a,start,mid)
                newNode.right= dfs(a,mid+1,end)
                return newNode
        array= sortedArray(head)
        return dfs(array,0,len(array))
    def mergeTwoBinary(self,root1,root2):
        if(root1 is None):
            return root2
        if(root2 is None):
            return root1
        root1.data +=root2.data
        left= self.mergeTwoBinary(root1.left, root2.left)
        right= self.mergeTwoBinary(root1.right, root2.right)
        root1.left= left
        root1.right= right
        return root1
    def printAllSingleChild(self,root):
        if(root is None):
            return
        
        if(root.left is None or root.right is None):
            if(root.left is None):
                print(root.left)
            if(root.right is None):
                print(root.right)
        left=self.printAllSingleChild(root.left)
        right= self.printAllSingleChild(root.right)
    def findCorresPondingNodeThatNode(self,root,cloned,target):
        if(root is None or cloned is None):
            return 
        c1= root
        c2= cloned
        s1= []
        s2= []
        while c1 is not None or len(s1) !=0:
            while c1 is not None:
                s1.append(c1)
                s2.append(c2)
                c1 = c1.left
                c2= c2.left
        c1= s1.pop()
        c2= s2.pop()
        if(c1.val==target.val):
            return True
        c1= c1.right
        c2= c2.right
        return

    def BSTfromInorderAndPreOrder(self,inorder,preOrder):
        def dfs(inorder,preOrder,pre_start,pre_end,in_start,in_end):
            if(in_start>in_end):
                return
            index=in_start
            while inorder[index] !=preOrder[pre_start]:
                index+=1
            lrange=index-in_start

            newNode= Node(preOrder[pre_start])
            newNode.left=dfs(inorder,preOrder,pre_start+1,pre_start+lrange,in_start,index-1)
            newNode.right=dfs(inorder,preOrder,pre_start+lrange+1,pre_end,index+1,in_end)
            return newNode
        return dfs(inorder,preOrder,0,len(preOrder)-1,0,len(inorder)-1)








                

        




    

            

        

b= BinaryTree()
callStack=[]
# tree= b.createTree([2,None,3,None,4,None,5,None,6])
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
n2.left= n5
n2.right=n6
n3.left=n7
n3.right=n8
n4.left=n9
n4.right=n10
# n5.left=n12
n5.right=n13

a= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]



count =1
b.printAllSingleChild(tree)
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(b.BSTfromInorderAndPreOrder(inorder,preorder))
# print(b.levelOrderTraversal(b.mergeTwoBinary(tree, b.SortedArrayToBinaryTree(a,0,len(a)))))
# print(b.levelOrderTraversal(b.SortedArrayToBinaryTree(a,0,len(a))))
# print(b.levelOfNode(tree,5,count))
# print(b.leftView(tree))
# print(b.verticalOrderTraversal(tree))
# print(b.paths(tree))
# b.pathsSum(tree)
# b.pathSumSecond(tree,12)
# callStack=[]
# b.binaryTreeCallStack(tree,callStack)
# print(callStack)
# print(b.nodeToRootPath(tree,5))
# path=[]
# paths=[]
# print(b.searchElementInTree(tree,9,path,paths))
# print(paths)
# print(b.fact(10))
# b.kthLevelDown(tree,2)
# path=[]
# paths= []
# sum=0
# b.leftClonedTree(tree)
# b.insertionLeft(tree,5)
# b.pathLeaveToRoot(tree,path,paths,sum)
# print(paths)
# b.traversal(tree)
# print(b.isCousins(tree,4,3))

# def factorial(n,callStack):
#     callStack.append(n)
#     print(callStack)
#     if(n==0):
#         callStack.pop()
#         print(callStack)
#         return 1
#     value= n*factorial(n-1,callStack)
#     callStack.pop()
#     print(callStack)
#     return value

# callStack=[]
# print(factorial(10,callStack))
