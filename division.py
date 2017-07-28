def division(a,b):
    temp = 1
    count =0
    if a<0 and b>0:
        temp = -1
        a = -a
    if b ==0:
        return None
    if b <0 and a>0:
        temp =-1
        b = -b
    if b<0 and a< 0:
        temp=1
        a = -a
        b= -b 
    while a>1:
        a =  a - b
        count = count + 1
    return count * temp

print division (6,2)
print division (-6,2)
print division (-9,-3)
