from heapq import heappush, heappop

def solution(land, height):
    n = len(land)
    visited = [[False] * n for _ in range(n)]
    heap = [(0, 0, 0)]  # gap, x, y
    answer = 0
    
    while heap:
        cost, x, y = heappop(heap)
        if visited[x][y]: continue
        
        visited[x][y] = True
        answer += cost
        
        for direction_x, direction_y in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_x = x + direction_x
            new_y = y + direction_y
            
            if (0 <= new_x < n) and (0 <= new_y < n) and not visited[new_x][new_y]:
                gap = abs(land[x][y] - land[new_x][new_y])
                if gap <= height: 
                    gap = 0
                heappush(heap, (gap, new_x, new_y))
    
    return answer
