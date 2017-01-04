#!/usr/bin/python
'''
Problem:
Hacker Rank - Knapsack
'''

### TODO ###
# max(1 + m[11], 6 + m[6], 9 + m[9])

T = int(input())
for t in range(T):
    N, K = [int(x) for x in input().split(' ')]
    elem = [int(x) for x in input().split(' ')]
    
    m = [0]
    for k in range(1, K+1):
        max_vals = [(x + m[k-x]) for x in elem if x <= k]
        if max_vals:
            m.append(max(max_vals))
        else:
            m.append(0)
        
    print(m[K])
    
'''
12
9
'''