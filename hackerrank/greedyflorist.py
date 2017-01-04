#!/usr/bin/python
'''
Problem:
Hacker Rank - Greedy Florist
'''

### TODO ###
from collections import deque
import heapq

N, K = (int(x) for x in input().split(' '))
cust = deque([0] * K)
heap = []

for x in input().split(' '):
    heapq.heappush(heap, -int(x))
    
totalCost = 0
for i in range(0,N):
    c = -heapq.heappop(heap)
    x = cust.popleft() + 1
    totalCost += x * c
    cust.append(x)
    
print(totalCost)

    
'''
13
15
'''