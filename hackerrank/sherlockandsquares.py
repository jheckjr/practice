'''
Problem:
Hacker Rank - Sherlock and Squares
'''

import sys
import math

def sherlock(f):
    t = int(f.readline().strip())
    output = []
    
    for i in xrange(t):
        l, h = [int(x) for x in f.readline().strip().split(' ')]
        in_range = True
        num = 0
        sqr = math.floor(math.sqrt(l))
        
        while(in_range):
            sqrd = sqr*sqr
            
            if l <= sqrd and sqrd <= h:
                num += 1
            if h <= sqrd:
                in_range = False
            
            sqr += 1
        
        output.append(num)
        
    return output
        
def test():
    with open('sherlockandsquares.txt', 'r') as f:
        result = sherlock(f)
        assert result == [2, 0]
        
    print("Test passed")

test()
