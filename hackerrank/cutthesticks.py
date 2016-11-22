'''
Problem:
Hacker Rank - Cut the Sticks
'''

import sys
import math

def cut(f):
    output = []
    n = int(f.readline().strip())
    arr = [int(arr_temp) for arr_temp in f.readline().strip().split(' ')]
    
    while arr:
        output.append(len(arr))
        arr.sort()
        minVal = arr[0]
        arr = [x - minVal for x in arr if x > minVal]
        
    return output
        
def test():
    with open('cutthesticks.txt', 'r') as f:
        result = cut(f)
        assert result == [8, 6, 4, 1]
        result = cut(f)
        assert result == [6, 4, 2, 1]
        
    print("Test passed")

test()
