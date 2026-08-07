from collections import deque

def bfs(start, target, maps):
    rowLen = len(maps)
    colLen = len(maps[0])
    visited = [[False] * colLen for _ in range(rowLen)]
    q = deque()
    
    q.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while q:
        curRow, curCol, dist = q.popleft()
        
        if (curRow, curCol) == target: return dist
        
        for directionRow, directionCol in directions:
            newRow, newCol = curRow + directionRow, curCol + directionCol
            if (0 <= newRow < rowLen and 0 <= newCol < colLen):
                if (not visited[newRow][newCol] and maps[newRow][newCol] != 'X'):
                    visited[newRow][newCol] = True
                    q.append((newRow, newCol, dist + 1))
    return -1


def solution(maps):
    rowLen = len(maps)
    colLen = len(maps[0])
    
    coordinates = {}
    for row in range(rowLen):
        for col in range(colLen):
            if (maps[row][col] in ('S', 'L', 'E')):
                coordinates[maps[row][col]] = (row, col)
    
    # S → L
    dist1 = bfs(coordinates['S'], coordinates['L'], maps)
    if dist1 == -1:
        return -1
    
    # L → E
    dist2 = bfs(coordinates['L'], coordinates['E'], maps)
    if dist2 == -1:
        return -1
    
    return dist1 + dist2
