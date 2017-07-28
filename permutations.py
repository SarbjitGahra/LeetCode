import math
def permutations(a):

    length = len(a)
    num = math.factorial(length)
    for i in range (0,num-1):
#       result.append((next_perm(a)))
        print next_perm(a)
def next_perm(a):
#step1 find a number thats breaks the ascending order of suffix
#starting from the end i.e 2 in this case [0,1,2,5,3,3,0]
    i = len(a) -1
    pivot=0
    while i>0:
        #print i, i-1, a[i], a[i-1]
        if a[i]> a[i-1]:
            pivot = i-1
            break
        i = i -1


#step 2 swap the pivot with the last number that is bigger than pivot in the list
#so it would be last 3 in our case
    swapped=-1
    for i in range (pivot + 1, len(a)):
        if a[i]>pivot:
            swapped =i


#step 3 swap both pivot with swapped
#0,1,3,5,3,2,0]
    #print "pivot", a[pivot], "swapped", a[swapped]
    swap(a,pivot, swapped )


#step 4 sort the part of the array between pivot and end
    b=a[pivot+1:]
    b.sort()
    #print b
    for i in range(pivot +1 , len(a)):
        a.pop()
    for j in range(0,len(b)):
        a.append(b[j])
    #print a
    return a



def swap(a,i,j):
    temp = a[i]
    a[i] =a[j]
    a[j] = temp
    return a

def sort(a,start_index, end_index):
    for i in range (end_index -1,start_index,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                swap(a, j+1,j)
    return a
print permutations([0,1,2])
print permutations(['a','b','c'])
