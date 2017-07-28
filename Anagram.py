def isAnagram(a,b):
    if len(a)!= len(b):
        return False
    a="".join(sorted(a))
    b="".join(sorted(b))
    if a==b:
        return True
    return False

print isAnagram("silent","listen")
