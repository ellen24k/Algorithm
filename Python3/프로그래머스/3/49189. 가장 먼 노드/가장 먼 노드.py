from collections import deque

def bfs(graph, node, visited):
    queue = deque([[node, 0]])
    visited[node] = 1
    # print(queue)
    
    while queue:
        [v,c] = queue.popleft()
        # print(v, c, graph[v])
        
        for index in graph[v]:
            if not (visited[index]):
                queue.append([index,c+1])
                visited[index] = c+1
    return visited

def solution(n, edge):
    
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    # print(edge)
    
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    # print(graph)
    #	[[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]
    
    distance = bfs(graph,1,visited)
    # print(distance)
    return distance.count(max(distance))