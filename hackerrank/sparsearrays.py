#!/usr/bin/python
'''
Problem:
Hacker Rank - Sparse Arrays
'''

### TODO ###
import sys
    
def process(f):
    table = {}
    n = int(input().strip())
    for i in range(0,n):
        new_str = input()
        
        if new_str in table:
            table[new_str] += 1
        else:
            table[new_str] = 1
            
    q = int(input().strip())
    for j in range(0,q):
        query = input()
        
        if query in table:
            print(table[query])
        else:
            print(0)
        
def test():
    with open('funnystring.txt', 'r') as f:
        result = process(f)
        assert result == [2, 1, 0]
        
    print("Test passed")

test()
