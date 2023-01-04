class PQueue:
    def __init__(self) -> None:
        self.queue=[]

    def add_data(self,k,d):
        if(len(self.queue)==0):
            self.queue.append((k,d))
        else:
            self.queue.append((k,d))
            for i in range(len(self.queue)//2-1,-1,-1):
                self.hepify(self.queue,len(self.queue),i)
    def hepify(self,a,n,i):
        # print(a) "min-heap"
        "TC= (n)"
        largest= i
        left= 2*i+1
        right= 2+i+2
        if(left<n and a[left]<a[largest]):
            largest= left
        if(right<n and a[right]<a[largest]):
            largest= right
        if(largest !=i):
            a[largest],a[i]= a[i],a[largest]
            self.hepify(a,n,largest)

    def show(self):
        print(self.queue)

pq= PQueue()
pq.add_data(1,5)
pq.add_data(11,6)
pq.add_data(21,7)
pq.add_data(31,9)
pq.add_data(41,3)
pq.add_data(51,10)
pq.add_data(61,11)
pq.add_data(71,17)
pq.show()

        
    
        