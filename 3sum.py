#To check if sum of three elements in an arraay equals to zero
#We are going to use binary search in the problem to find our solution
#first pointer will be our i, second pointer will be l =i + 1 and
#last one will be r= length -1
#if sum of three pointers is more than 0 we will decrement from behind
#if the sum of three pointers is less than 0 we increment l
def three_sum(a):
    #Array to store the results of the three elements
    result =[]
    a.sort()
    length = len(a)
    for i in range (0,length -2):
        #if you see same element skip ahead
        if i > 0 and a[i] == a[i-1]:
            continue
        i = i + 1
        l=i+ 1
        r = length -1
        sum = a[i] + a[l]  + a[r]
        while l < r :
            if sum ==0:
                result.append((a[i],a[l], a[r]))
                l = l+ 1
                r = r-1
            elif sum <0:
                l = l+ 1
            else:
                r = r-1
        return result

print three_sum([-1,0,1,2,-1,-4])
