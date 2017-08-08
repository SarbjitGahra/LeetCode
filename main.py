from threestacksinarray import threestacks

if __name__ == '__main__':
    ts = threestacks(6)
    ts.push(0,1)
    ts.push(1,2)
    ts.push(2,3)
    ts.push(1,5)
    ts.push(0,9)
    ts.push(0,18)

    ts.print_stack()
    ts.pop(0)
    ts.pop(1)
    ts.pop(2)
    ts.print_stack()
    ts.push(0,17)
    ts.push(2,18)
    ts.print_stack()
