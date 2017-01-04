#!/usr/bin/python
'''
Problem:
Hacker Rank - Maximum Subarray
'''

### TODO ###
# non-contiguous (add all positive elements or find smallest negative)
# contiguous ()
testCases = int(input())

for i in range(0,testCases):
    N = int(input())
    array = [int(x) for x in input().split(' ')]
    
    noncontsum = sum([x for x in array if 0 < x])
    # no positive numbers
    if noncontsum == 0:
        noncontsum = max(array)
        print(str(noncontsum) + ' ' + str(noncontsum))
        continue
    
    max_here = 0
    max_seen = 0
    
    for num in array:
        max_here = max(0, max_here + num)
        max_seen = max(max_seen, max_here)
        
    print(str(max_seen) + ' ' + str(noncontsum))
    
    
'''
10 10
10 11
'''