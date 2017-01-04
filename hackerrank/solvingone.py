'''
Problem:
Hacker Rank - Solving one problem with another
'''

### TODO ###
# Get original N, M, K
# Build array of tuples for each pair (min, max)
# Get E (M lines)
# Remove each edge (u,v) from array when received
# Print N, M', K'
# Print each tuple in array

N, M, K = [int(x) for x in input().split(' ')]
complement = []

for u in range(N):
    for v in range(u + 1, N):
        complement.append((u, v))
        
for i in range(M):
    u, v = (int(x) for x in input().split(' '))
    complement.remove((min(u,v), max(u,v)))
    
print(N, len(complement), N-K)
for i in complement:
    print(i[0], i[1])

'''
3 1 1
1 2
'''