#!/usr/bin/python
'''
Problem:
Hacker Rank - Longest Common Subsequence
'''

### TODO ###

N, M = [int(x) for x in input().split(' ')]
A = [int(x) for x in input().split(' ')]
B = [int(x) for x in input().split(' ')]

# M for row, N for col
lcs_len = [[0 for x in range(N+1)] for y in range(M+1)]

for i in range(1, M+1):
    for j in range(1, N+1):
        if A[j-1] == B[i-1]:
            lcs_len[i][j] = lcs_len[i-1][j-1] + 1
        else:
            lcs_len[i][j] = max(lcs_len[i-1][j], lcs_len[i][j-1])
            
i = M
j = N
lcs = []
while 0 < lcs_len[i][j]:
    if lcs_len[i-1][j-1] == max(lcs_len[i-1][j-1], lcs_len[i-1][j], lcs_len[i][j-1]) and lcs_len[i-1][j-1] < lcs_len[i][j]:
        lcs.append(A[j-1])
        i -= 1
        j -= 1
    elif lcs_len[i-1][j] < lcs_len[i][j-1]:
        j -= 1
    else:
        i -= 1
    
lcs.reverse()
print(' '.join(map(str, lcs)))
    
'''
1 2 3
'''