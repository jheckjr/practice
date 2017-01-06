'''
Problem:
Hacker Rank - Cipher
'''

def solve(f):
    N, K = [int(x) for x in f.readline().split(' ')]
    S = [int(x) for x in list(f.readline())]
    
    # number of ones in last K-1 bits
    numOnes = S[0]
    B = [0] * N
    B[0] = S[0]
    
    for i in range(1,N):
        B[i] = (numOnes % 2) ^ S[i]
        numOnes += B[i]
        
        if K-1 <= i:
            numOnes -= B[i-(K-1)]
        
    return ''.join([str(x) for x in B])

def test():
    with open('cipher.txt', 'r') as f:
        result = solve(f)
        assert result == '1001010'
        
    print("Test passed")

test()