import math


# smallest min, max value in python  -math.inf and math.inf


def max_value(v1, v2):
    if(v1>v2):
        return v1
    return v2
def min_value(v1, v2):
    if(v1>v2):
        return v2
    return v1

class BinaryNode:
    def __init__(self,data) -> None:
        self.left= None
        self.right= None
        self.data= data
    def inorderTraversal(self,list1):
        if(list1 is not None):
            self.inorderTraversal(list1.left)
            print(list1.data,end="->")
            self.inorderTraversal(list1.right)
    def PostOrderTraversal(self,list1):
        if(list1 is not None):
            self.PostOrderTraversal(list1.left)
            self.PostOrderTraversal(list1.right)
            print(list1.data, end="->")
    def preOrderTraversal(self,list1):
        if(list1 is not None):
            print(list1.data, end="->")
            self.preOrderTraversal(self.left)
            self.preOrderTraversal(self.right)
    def size(self,list1):
        if(list1 is None):
            return 0
        ls= self.size(list1.left)
        rs= self.size(list1.right)
        return ls+rs+1
    def sum(self,list1):
        if(list1 is None):
            return 0
        ls= self.sum(list1.left)
        rs= self.sum(list1.right)
        return ls+rs+list1.data
    def height(self, list1):
        if(list1 is None):
            return 0
        lh= self.height(list1.left)
        rh= self.height(list1.right)
        return lh+rh+1
    def max(self,list1):
        if(list1 is None):
            return -math.inf

        left_max = self.max(list1.left)
        right_max= self.max(list1.right)
        return max_value(max_value(left_max,right_max),list1.data)
    def min(self,list1):
        if(list1 is None):
            return math.inf
        left_min= self.min(list1.left)
        right_min= self.min(list1.right)
        return min_value(min_value(left_min, right_min),list1.data)
    def traversal(self,list1):
        if(list1 is None):
            return 
        print("Pre",list1.data)
        self.traversal(list1.left)
        print("In",list1.data)
        self.traversal(list1.right)
        print("Post",list1.data)
    def level_order_traversal(self,list1):
        queue=[]
        queue.append(list1)
        while len(queue)>0:
            node= queue.remove(queue[0])
            print(node)
            if(node.left is not None):
                queue.append(node.left)
            if(node.right is not None):
                queue.append(node.right)
        print()





    
        



# binary= BinaryNode()
n1= BinaryNode(1)
n2= BinaryNode(2)
n3= BinaryNode(3)
n4= BinaryNode(4)
n5= BinaryNode(5000)
n6= BinaryNode(6)
n7= BinaryNode(800)
n8= BinaryNode(8)
n9= BinaryNode(9)
n10= BinaryNode(10)
n11= BinaryNode(11)
n12= BinaryNode(12)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7
n4.left=n8
n5.left=n10
n10.left=n11
n11.left=n12

# n1.inorderTraversal(n1)
# n1.PostOrderTraversal(n1)
# n1.preOrderTraversal(n1)
# print(n1.size(n1))
# print(n1.sum(n1))
# print(n1.height(n1))
# print(n1.max(n1))
# print(n1.min(n1))
# print(n1.traversal(n1))
# print(n1.level_order_traversal(n1))
print(True-True)