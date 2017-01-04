#!/usr/bin/python
'''
Problem:
Hacker Rank - Jim and the Orders
'''

### TODO ###
from heapq import *

N = int(input())
heap = []

for i in range(1,N+1):
    time = sum([int(x) for x in input().split(' ')])
    heappush(heap, (time, i)) 
    
while heap:
    finOrders = []
    finTime, orderNum = heappop(heap)
    heappush(finOrders, orderNum)
    
    while heap and heap[0][0] == finTime:
        heappush(finOrders, heappop(heap)[1])
        
    while finOrders:
        print(heappop(finOrders), end=' ')
    
    
'''
123

4 2 5 1 3
'''