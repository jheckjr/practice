#!/usr/bin/python
'''
Problem:
Hacker Rank - Truck Tour
'''

### TODO ###
import sys
import heapq
    
def process(f):
    n = int(input().strip())
    stack = []
    heap = []
    
    def add(num):
        stack.append(num)
        heapq.heappush(heap, -num)
        
    def remove():
        num = stack.pop()
        heap.remove(-num)
        heapq.heapify(heap)
        
    def print_max():
        print(-heap[0])
        
    for i in range(0,n):
        query = input().strip().split()
        if query[0] == '1':
            add(int(query[1]))
        elif query[0] == '2':
            remove()
        elif query[0] == '3':
            print_max()
        
def test():
    with open('funnystring.txt', 'r') as f:
        result = process(f)
        assert result == [26, 91]
        
    print("Test passed")

test()
