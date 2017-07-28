#remove duplicates from an array in place without using extra data structure
def duplicates(a):
    last_index=0
    for current in range (1 , len(a)):
        if a[current]== a[last_index]:
            continue
        else:
            last_index = last_index + 1
            a[last_index] = a [current]

#once first last_index + 1 positions have been filled with unique elements.
#rest are duplicates and could be removed
    if len(a) > last_index+1:
        for i in range (last_index +1 , len(a)):
            a.pop()
    return a

print duplicates([1,2,3,3])
print duplicates([1,2,2,2,3,3])
print duplicates([1,1,1,1,1,2,2,2,2,2,3,3])
