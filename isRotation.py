def isRotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    s2=s2+s2
    return isSubstring(s1,s2)    

def isSubstring(s1,s2):
    if s1 in s2:
        return True
    return False
print isRotation("abc", "cab")
