'''
Problem:
Hacker Rank - BFS Shortest Reach
'''

# Perform breadth-first search and return the distance from the start vertex to
# each vertex in the graph as a multiple of 6
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
                found = graph[vertex] - set(explored.keys())
                queue.extend(found)
                distances.extend([(dist+6) for x in found])
            
    return explored   

# Return the distances (multiples of 6) from the start vertex to each vertex in 
# the graph or -1 if the start vertex
def getDist(vertices, num, start):
    result = []
    for i in range(1,num+1):
        if i != start:
            if i in vertices.keys():
                result.append(vertices[i])
            else:
                result.append(-1)
    
    return result
    
def solve(f):
    num_tests = int(f.readline().strip())
    result = []
    
    for i in range(num_tests):
        N, M = [int(x) for x in f.readline().strip().split(' ')]
        graph = {} 
        
        for j in range(0,M):
            first, second = [int(x) for x in f.readline().strip().split(' ')]
            
            if first in graph:
                graph[first].add(second)  
            else:
                graph[first] = {second}
                
            if second in graph:
                graph[second].add(first)  
            else:
                graph[second] = {first}
            
        start = int(f.readline().strip())
        result.append(getDist(bfs(graph, start), N, start))
        
    return result
    
def test():
    with open('bfs_shortestreach.txt', 'r') as f:
        result = solve(f)
        assert result[0] == [6, 6, -1]
        assert result[1] == [-1, 6]
        
    print("Test passed")
    
test()