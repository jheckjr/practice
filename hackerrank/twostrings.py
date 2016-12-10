'''
Problem:
Hacker Rank - Two Strings
'''

import sys

def process(f):
    output = []
    n = int(f.readline().strip())
    
    for i in range(n):
        strA = f.readline().strip()
        strB = f.readline().strip()
        
        for char in strB:
            if char in strA:
                output.append("YES")
                break
        
        if len(output) < i + 1:
            output.append("NO")
        
    return output
        
def test():
    with open('twostrings.txt', 'r') as f:
        result = process(f)
        assert result == ["YES", "NO"]
        
    print("Test passed")

test()
