class Queue:
    def __init__(self) -> None:
        self.queue= []

    def add_item(self,d):
        self.queue.append(d)


    def delete(self):
        if(len(self.queue)==0):
            return "queue is Null"
        value=self.queue.pop(0)
        return value
    def show(self):
        return self.queue


q= Queue()
q.add_item(5)
q.add_item(4)
q.add_item(7)
q.add_item(6)
q.add_item(8)
q.add_item(12)
print(q.show())
print(q.delete())
print(q.show())






    