def dups(a):
    if len(a) ==0:
        return None
    if len(a)==1:
        return True
    a="".join(sorted(a))
    print a
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            return False
    return True


print dups('abc')
print dups('abcda')
print dups('abcdabbdeeff')
