class Union:
    def __init__(self,array):
        self.parent= {}
        self.rank= {}
        for i in array:
            self.parent[i]= i
            self.rank[i]=0
    def find(self,k):
        if(self.parent[k] !=k):
            self.parent[k]= self.find(self.parent[k])
        return self.parent[k]

    def union(self,a,b):
        x= self.find(a)
        y= self.find(b)

        if(x ==y):
            return 
        if(self.rank[x]>self.rank[y]):
            self.rank[y]= x
        elif(self.rank[y]>self.rank[x]):
            self.rank[x]= y
        else:
            self.rank[x]=y
            self.rank[y]= self.rank[y]+1

    def print_union(self,univers):
        print([self.find(i) for i in univers])


a=[1,2,3,4,5]
df= Union(a)
df.union(4,3)
df.print_union(a)
df.union(2,1)
df.print_union(a)
df.union(1,3)
df.print_union(a)
