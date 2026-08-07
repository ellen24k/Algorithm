def solution(n):
    direction = {'r': [0, 1], 'd': [1, 0], 'l': [0, -1], 'u': [-1, 0]}
    answer = [[0] * n for i in range(n)]
    cur = [0, 0]
    num = 1
    
    for i in range(n, 0, -2):
        for dir in direction:
            for r in range(i - 1):
                answer[cur[0]][cur[1]] = num
                cur[0] += direction[dir][0]
                cur[1] += direction[dir][1]
                num += 1
        cur[0] += 1
        cur[1] += 1
    if (n  % 2 == 1): answer[cur[0] - 1][cur[1] - 1] = num
    
    return answer