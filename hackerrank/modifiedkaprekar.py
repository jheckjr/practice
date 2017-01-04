#!/usr/bin/python
'''
Problem:
Hacker Rank - Modified Kaprekar Numbers
'''

### TODO ###

import sys
    
def process(f):
    p = int(input().strip())
    q = int(input().strip()) + 1
    
    count = 0
    
    for i in range(p,q):
        square = i*i
        num_digits = len(str(square))
        sum = 0
        
        if num_digits == 1:
            sum = square
        else:
            if num_digits % 2 == 0:
                l = int(str(square)[:int(num_digits/2)])
                r = int(str(square)[int(num_digits/2):num_digits])
            else:
                l = int(str(square)[:int(num_digits/2)])
                r = int(str(square)[int(num_digits/2):num_digits])
            sum = l + r
        
        if sum == i:
            print(i, end=' ')
            count += 1
    
    if count == 0:
        print('INVALID RANGE')
        
def test():
    with open('funnystring.txt', 'r') as f:
        result = process(f)
        assert result == [1, 9, 45, 55, 99]
        
    print("Test passed")

test()
