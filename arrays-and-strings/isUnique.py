''''
Problem:
Determine if a string is composed of unique characters.
Assumptions:
String is composed of ASCII characters.
'''

def isUnique(s):
    if len(s) > 128:
        return False
        
    arr = [0] * 128
    
    for c in s:
        if arr[ord(c)]:
            return False
        else:
            arr[ord(c)] = 1
    
    return True
    
# Assume you cannot create a new data structure
def isUnique2(s):
    if len(s) > 128:
        return False
        
    for i in xrange(len(s)):
        for j in xrange(i+1,len(s)):
            if s[i] == s[j]:
                return False
    
    return True
    
def test():
    s = "Hello World"
    assert isUnique(s) == False
    
    s = "abcdEfghIjk!"
    assert isUnique(s) == True
    
    s = ""
    assert isUnique(s) == True
    print("Test passed")
    
def test2():
    s = "Hello World"
    assert isUnique(s) == False
    
    s = "abcdEfghIjk!"
    assert isUnique(s) == True
    
    s = ""
    assert isUnique(s) == True
    print("Test2 passed")
    
test()
test2()
