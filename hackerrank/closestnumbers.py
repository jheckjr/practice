#!/usr/bin/python
'''
Problem:
Hacker Rank - Closest Numbers
'''

import heapq
import sys
    
def process(f):
    n = int(f.readline().strip())
    heap = [int(x) for x in f.readline().strip().split()]
    output = []
    
    heapq.heapify(heap)
    min_diff = heap[1] - heap[0]
    first = heapq.heappop(heap)
    
    for i in range(1,n):
        second = heapq.heappop(heap)
        diff = second - first
        
        if min_diff < diff:
            first = second
            continue
        elif diff < min_diff:
            min_diff = diff
            output = []
            
        output.append(first)
        output.append(second)
        first = second
        
    return output
        
def test():
    with open('closestnumbers.txt', 'r') as f:
        result = process(f)
        assert result == [-20, 30]
        result = process(f)
        assert result == [-520, -470, -20, 30]
        result = process(f)
        assert result == [2, 3, 3, 4, 4, 5]
        
    print("Test passed")

test()
