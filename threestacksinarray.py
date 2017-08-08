#three stacks in one array
class threestacks:
    def __init__(self,size):
        self.lst = [-1]* size
        self.stack1_head = -1
        self.stack2_head = -1
        self.stack3_head = -1
        self.next_available=0
        # stacks ={0:"stack_0" , 1:"stack_1" , 2:"stack_2"}
        self.stack1=""
        self.stack2=""
        self.stack3=""
        self.next_available=0

    def push(self,stack,value):

        if self.next_available <len(self.lst):
            self.lst[self.next_available]=value

            if stack ==0:
                self.stack1= self.stack1 + str(self.next_available)
                self.next_available +=1
                self.stack1_head=int(self.stack1[-1])
            elif stack ==1:
                self.stack2= self.stack2 + str(self.next_available)
                self.next_available +=1
                self.stack2_head=int(self.stack2[-1])
            else:
                self.stack3= self.stack3 + str(self.next_available)
                self.next_available +=1
                self.stack3_head=int(self.stack3[-1])
    def print_stack(self):
        #print " ihello its working"
        print self.lst
    def pop(self,stack):
        if stack ==0:
            self.lst[int(self.stack1_head)]=-1
            self.next_available=self.stack1_head
            self.stack1_head = str(int(self.stack1_head/10))
        elif stack ==1:
            self.lst[int(self.stack2_head)]=-1
            self.next_available=self.stack1_head
            self.stack2_head = str(int(self.stack2_head/10))
        else:
            self.lst[int(self.stack3_head)]=-1
            self.next_available=self.stack3_head
            self.stack3_head = str(int(self.stack3_head/10))
