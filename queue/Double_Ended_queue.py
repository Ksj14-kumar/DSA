class DQueue:
    def __init__(self):
        self.queue=[]

    def add_item_from_rear(self,d):
        self.queue.append(d)
    def add_item_from_front(self,d):
        self.queue.insert(0,d)
    def remove_item_from_front_side(self):
        if(len(self.queue)==0):
            return 
        value=self.queue.pop(0)
        return value
    def remove_item_from_backside(self):
        if(len(self.queue)==0):
            return
        value= self.queue.pop()
        return value

    def show(self):
        print(self.queue)

dq= DQueue()
dq.add_item_from_front(8)
dq.add_item_from_front(9)
dq.add_item_from_front(10)
dq.add_item_from_rear(4)
dq.add_item_from_rear(2)
dq.show()
dq.remove_item_from_backside()
dq.show()
dq.remove_item_from_front_side()
dq.show()

    