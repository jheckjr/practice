#!/usr/bin/python
'''
Problem:
Hacker Rank - Minimum Average Waiting Time
'''

### TODO ###
from collections import deque
import heapq

N = int(input())
# min heap of unarrived customers based on order time
orderHeap = []

for x in range(0,N):
    orderTime, cookTime = (int(i) for i in input().split(' '))
    heapq.heappush(orderHeap, (orderTime, cookTime))

# min heap of waiting customers based on cook time
firstCust = heapq.heappop(orderHeap)
cookHeap = [(firstCust[1], firstCust[0])]
waitTime = 0
currentTime = firstCust[0]

# put all waiting customers in the heap
while orderHeap:
    nextCust = (orderHeap[0][1], orderHeap[0][0])
    
    if nextCust[1] <= currentTime:
        heapq.heappush(cookHeap, nextCust)
        heapq.heappop(orderHeap)
    else:
        break

while cookHeap or orderHeap:
    currCust = heapq.heappop(cookHeap)
    # add cook time
    #if currentTime != currCust[0]:
    currentTime += currCust[0]
    # current time - arrival time
    waitTime += currentTime - currCust[1]
    
    # put all waiting customers in the heap
    while orderHeap:
        nextCust = (orderHeap[0][1], orderHeap[0][0])
        
        if nextCust[1] <= currentTime:
            heapq.heappush(cookHeap, nextCust)
            heapq.heappop(orderHeap)
        elif not cookHeap:
            heapq.heappush(cookHeap, nextCust)
            currentTime = nextCust[1]
            heapq.heappop(orderHeap)
        else:
            break

print(str(int(waitTime/N)))
    
'''
9

8

'''