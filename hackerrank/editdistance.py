#!/usr/bin/python
'''
Problem:
Hacker Rank - Edit Distance
'''

### TODO ###
N = int(input())

for i in range(0, N):
    str1 = input()
    str1_len = len(str1) + 1
    str2 = input()
    str2_len = len(str2) + 1
    
    dist_table = [[0 for x in range(str1_len)] for y in range(str2_len)]

    for r in range(1, str2_len):
        dist_table[r][0] = r
        
    for c in range(1, str1_len):
        dist_table[0][c] = c
        
    for row in range(1, str2_len):
        for col in range(1, str1_len):
            same_char = 1

            if str1[col-1] == str2[row-1]:
                same_char = 0
            
            dist_table[row][col] = min(dist_table[row-1][col-1] + same_char,
                                       dist_table[row][col-1] + 1,
                                       dist_table[row-1][col] + 1)
                
    print(dist_table[str2_len-1][str1_len-1])
    
    
'''
1
'''