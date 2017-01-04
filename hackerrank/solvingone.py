'''
Problem:
Hacker Rank - Solving one problem with another
'''

def solve(f):
    # Get N, M, and K
    N, M, K = [int(x) for x in f.readline().strip().split(' ')]
    complement = []
    
    # Create list of pairs between each caller 0 to N-1
    for u in range(N):
        for v in range(u + 1, N):
            complement.append((u, v))
            
    # Remove each pair given in the input to get a complement of the input graph
    for i in range(M):
        u, v = (int(x) for x in f.readline().strip().split(' '))
        complement.remove((min(u,v), max(u,v)))
        
    # Add resulting N, M', and K' to result
    result = [[N, len(complement), N-K]]
    
    # Add each pair in the complement graph to the result
    for i in complement:
        result.append([i[0], i[1]])
        
    return result

def test():
    with open('solvingone.txt', 'r') as f:
        result = solve(f)
        assert result[0] == [3, 1, 1]
        assert result[1] == [1, 2]
        
    print("Test passed")
    
test()
