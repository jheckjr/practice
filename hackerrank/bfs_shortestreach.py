'''
Problem:
Hacker Rank - BFS Shortest Reach
'''

### TODO ###
def bfs(graph, start):
    queue = [start]
    distances = [0]
    explored = {}
    
    if start in graph.keys():
        while queue:
            vertex = queue.pop(0)
            dist = distances.pop(0)

            if vertex not in explored:
                explored[vertex] = dist
                found = graph[vertex] - explored.keys()
                queue.extend(found)
                distances.extend([(dist+6) for x in found])
            
    return explored   

def printDist(vertices, num, start):
    for i in range(1,num+1):
        if i != start:
            if i in vertices.keys():
                print(vertices[i], end=' ')
            else:
                print('-1', end=' ')
    print()
    
Q = int(input())

for i in range(0,Q):
    N, M = [int(x) for x in input().split(' ')]
    graph = {} 
    
    for j in range(0,M):
        first, second = [int(x) for x in input().split(' ')]
        
        if first in graph:
            graph[first].add(second)  
        else:
            graph[first] = {second}
        if second in graph:
            graph[second].add(first)  
        else:
            graph[second] = {first}
        
    start = int(input())
    printDist(bfs(graph, start), N, start)
    
    
'''
6 6 -1
-1 6
'''