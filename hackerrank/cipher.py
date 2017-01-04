'''
Problem:
Hacker Rank - Cipher
'''

### TODO ###
N, K = [int(x) for x in input().split(' ')]
S = [int(x) for x in list(input())]

# number of ones in last K-1 bits
numOnes = S[0]
B = [0] * N
B[0] = S[0]

for i in range(1,N):
    B[i] = (numOnes % 2) ^ S[i]
    numOnes += B[i]
    
    if K-1 <= i:
        numOnes -= B[i-(K-1)]
    
print(''.join([str(x) for x in B]))

'''
1001010
'''