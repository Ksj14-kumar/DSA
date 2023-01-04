import heapq


class Heap:
    def __init__(self):
        self.queue= []



    def addItems(self,data):
        if len(self.queue)==0:
            self.queue.append(data)

        else:
            self.queue.append(data)
            for i in range(len(self.queue)//2-1,-1,-1):
                self.hepify(len(self.queue),self.queue,i)


    def remove_items(self,item):
        if item not in self.queue or len(self.queue)==0:
            return
        self.queue.remove(item)
        for i in range(len(self.queue)//2-1,-1,-1):
            self.hepify(len(self.queue),self.queue,i)
            

            
    def hepify(self,l,a,index):
        larget= index
        right= 2*index+2
        left= 2*index+1

        if left<l and  a[left]>a[larget]:
            larget= left
        if right<l  and a[right]>a[larget]:
            larget= right
        if larget !=index:
            a[larget],a[index]= a[index],a[larget]
            self.hepify(l,a,larget)

    def display(self):
        print(self.queue)

    def kth_largest(self,k):
        if len(self.queue)==0:
            return 
        if k>len(self.queue):
            return
        return self.queue[k]
            
