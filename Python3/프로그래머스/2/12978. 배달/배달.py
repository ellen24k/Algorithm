from heapq import heappop, heappush
from collections import defaultdict

def solution(N, road, K):
    road.sort(key=lambda x: (x[0], x[2]))
    dist_with_1 = [float('inf')] * N
    linked = defaultdict(list)
    nodes = [] # 1번 마을  -> 0번 노드

    for r in road:
        linked[r[0] - 1].append((r[1] - 1, r[2]))
        linked[r[1] - 1].append((r[0] - 1, r[2]))
        
    heappush(nodes, (0, 0))
    dist_with_1[0] = 0
    
    while nodes:
        dist, conn_node = heappop(nodes)
        
        if dist > dist_with_1[conn_node]: continue
            
        for n, d in linked[conn_node]:
            new_d = dist + d
            if new_d < dist_with_1[n]:
                dist_with_1[n] = new_d
                heappush(nodes, (new_d, n))
    
    return sum(1 for d in dist_with_1 if d <= K)