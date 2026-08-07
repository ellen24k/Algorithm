def solution(park, routes):
    h = len(park)
    w = len(park[0])
    
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j
    
    directions = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    
    for route in routes:
        op, n = route.split()
        n = int(n)
        dx, dy = directions[op]
        
        nx, ny = x, y
        valid = True
        
        for _ in range(n):
            nx += dx
            ny += dy
            
            if not (0 <= nx < h and 0 <= ny < w):
                valid = False
                break
            
            if park[nx][ny] == 'X':
                valid = False
                break
        
        if valid: x, y = nx, ny
    
    return [x, y]