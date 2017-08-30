#implementing que using two stacks
class stack:
    def __init__(self):
        self.lst=[]
        self.size =0


    def push(self,val):
        self.lst.append(val)

    def pop(self):
        temp = self.lst.pop()
        return temp
    def peek(self):
        temp = self.lst[-1]
    def print_stack(self):
        for i in  self.lst:
            print i
    def isEmpty(self):
        return len(self.lst)==0
class myQueue:
    def __init__(self):
        self.inbox = stack()
        self.outbox=stack()

    def enqueue(self, val):
        self.inbox.push(val)

    def dequeue(self):
        while not self.inbox.isEmpty():
            self.outbox.push(self.inbox.pop())

        return self.outbox.pop()


mq =myQueue()
mq.enqueue(1)
mq.enqueue(3)
mq.enqueue(4)
mq.enqueue(5)
mq.enqueue(6)
print (mq.dequeue())
print (mq.dequeue())
