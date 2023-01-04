# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Pair:
    def __init__(self,isBST,minV,maxV):
        self.isBST=isBST
        self.minV= minV
        self.maxV= maxV
class Solution:
    def isValidBST(self, root) -> bool:
        "Method=1"
        "using morris traversal"
        def dfs(root):
            curr= root
            pre=None
            while curr is not None:
                left =curr.left
                if(left is None):
                    if(pre is not None and pre.val>=curr.val):
                        return False
                    pre=curr
                    curr=curr.right
                    
                if(left is not None):
                    rightMost= self.getRightMost(left,curr)
                    if(rightMost.right is None):
                        rightMost.right=curr
                        curr=curr.left
                    else:
                        rightMost.right=None
                        if(pre is not None and pre.val>=curr.val):
                            return False
                        pre=curr
                        curr=curr.right
            return True
        return dfs(root)
    def getRightMost(self,l,c):
        while l.right is not None and l.right !=c:
            l= l.right
        return l
        
        
        # "Method-2"
        # "using path, inorder,traversal"
        # def dfs(root,path):
        #     if(root is None):
        #         return
        #     dfs(root.left,path)
        #     path.append(root.val)
        #     dfs(root.right,path)
        
        # path=[]
        # dfs(root,path)
        # print(path)
        # for i in range(1,len(path)):
        #     if(path[i]<=path[i-1]):
        #         return False
        # return True
    
    
        "Method-3"
        "Simple recursive"
#         def dfs(root):
#             if(root is None):
#                 return Pair(True,float('inf'),-float('inf'))

#             lp= dfs(root.left)
#             rp= dfs(root.right)
#             print( lp.isBST,rp.isBST,(root.val>lp.maxV and root.val<rp.minV))
#             isBST= lp.isBST and rp.isBST and (root.val>lp.maxV and root.val<rp.minV)
#             maxValue= max(root.val,max(lp.maxV,rp.maxV))
#             minValue= min(root.val,min(lp.minV,rp.minV))
#             # print(isBST)
#             return Pair(isBST,minValue,maxValue)
        
#         value= dfs(root)
#         return value.isBST



                
        
        
    
        
            
            
        
        
  
        
        
                
                
        
        
        
        

        
        