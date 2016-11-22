'''
Problem:
Hacker Rank - Utopian Tree
'''

import sys

def utopianTree(f):
    t = int(f.readline().strip())
    output = []
    
    for a0 in xrange(t):
        n = int(f.readline().strip()) - 1
    
        if n < 0:
            output.append(1)
        else:
            h = 2**(int(n/2) + 2) - 2 + (n % 2)
            output.append(h)
    return output
        
def test():
    with open('utopianTree.txt', 'r') as f:
        result = utopianTree(f)
        assert result == [1, 2, 7]
        
    print("Test passed")

test()
