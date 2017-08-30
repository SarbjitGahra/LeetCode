#towers of hanoi
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



def main():
    #toh(3,stack(), stack(),stack())
    toh_2(3,stack(), stack(),stack())

def toh(n,beg,aux, end):
    beg , aux , end = stack(), stack(), stack()
    for i in range(1,4):
        beg.push(i)

    #step1 move the smallest to destination peg
    print "moving {} to end ".format(beg.peek())
    end.push(beg.pop())

    #step2 move the second smallest to middle

    aux.push(beg.pop())

    #step3 move the smallest to the middle now

    aux.push(end.pop())

    #step4 move the biggest to the end now

    end.push(beg.pop())

    #step5 move the smallest back to first one now
    beg.push(aux.pop())

    #step6 move the second biggest on top of biggest

    end.push(aux.pop())

    #step7 move the smallest on top of the last peg

    end.push(beg.pop())
   #last peg should have all the disks in ascending order
    end.print_stack()
def toh_2(n,beg,aux, end):
    beg , aux , end = stack(), stack(), stack()
    for i in range(1,4):
        beg.push(i)
    for i in range(1,8):
        if i % 3 ==1:
            end.push(beg.pop())
        elif i % 3 ==2:
            aux.push(beg.pop())
        elif i %3 ==0:
                end.push(aux.pop)
    end.print_stack()
main()
