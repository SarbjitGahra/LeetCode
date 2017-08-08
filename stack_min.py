#find the min in stacks
import sys
class stack_min:
    def __init__(self,size):
        self.lst = []
        self.min=sys.maxint


    def push(self, value):
        self.lst.append(value)
        if value<self.min:
            self.min = value

    def pop(self):
        self.lst.pop()

    def min_stack(self):
        return self.min
    def print_stack(self):
        print self.lst

sm =stack_min(4)
sm.push(18)
sm.push(2)
sm.push(-1)
sm.push(0)
print sm.min_stack()
sm.print_stack()
