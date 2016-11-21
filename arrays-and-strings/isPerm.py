''''
Problem:
Determine if two strings are permutations.
Assumptions:
String is composed of lower 128 ASCII characters.
Capitalization matters.
'''

def isPerm(s1, s2):
    if len(s1) != len(s2):
        return False
        
    arr1 = [0] * 128
    arr2 = [0] * 128
    
    for c, d in zip(s1, s2):
        arr1[ord(c)] += 1
        arr2[ord(d)] += 1
        
    for i in xrange(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    
    return True
    
def test():
    s1 = "read"
    s2 = "dear"
    assert isPerm(s1, s2) == True
    
    s1 = "read"
    s2 = "red"
    assert isPerm(s1, s2) == False
    
    s1 = "read"
    s2 = "race"
    assert isPerm(s1, s2) == False
    
    s1 = "Read"
    s2 = "read"
    assert isPerm(s1, s2) == False
    print("Test passed")
    
test()
