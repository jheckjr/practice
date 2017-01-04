#!/usr/bin/python
'''
Problem:
Hacker Rank - Truck Tour
'''

### TODO ###
import sys
    
def process(f):
    n = int(input().strip())
    stops = []
    # do I only need amount deficient?
    for i in range(0, n):
        fuel, dist = [int(x) for x in input().strip().split(' ')][:2]
        stops.append((fuel - dist, fuel, dist))
        
    # look for negative values in the list for starting points and add values (shouldn't become positive)
    for j in range(0, n):
        index = j + 1
        if n == index:
            index = 0
            
        if stops[j][0] >= 0:
            fuel = stops[j][0]
            while index != j:
                if fuel < 0:
                    break
                    
                fuel += stops[index][0]
                
                index += 1
                if n == index:
                    index = 0
        
        if index == j:
            print(j)
            break
        
def test():
    with open('funnystring.txt', 'r') as f:
        result = process(f)
        assert result == [1]
        
    print("Test passed")

test()
