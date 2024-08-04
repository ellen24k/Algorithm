from collections import defaultdict, deque

def solution(land):
    answer = [0 for _ in range(len(land[0]))]
    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    # visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    
    def bfs(row, col, count):
        visited[row][col] = 1
        queue = deque([(row,col)])
        one_oil = {col}
    
        weight_r = (0,1,0,-1)
        weight_c = (1,0,-1,0)
    
        while(queue):
            r,c = queue.popleft()
        
            for i in range(4):
                new_row = r + weight_r[i]
                new_col = c + weight_c[i]
            
                if new_row >= 0 and new_row < len(land):
                    if new_col >= 0 and new_col < len(land[0]):
                        if land[new_row][new_col] == 1 and not visited[new_row][new_col]:
                            visited[new_row][new_col] = 1
                            queue.append((new_row, new_col))
                            count += 1
                            if new_col not in one_oil: one_oil.add(new_col)
                        
        # print(one_oil, count)
        # for v in visited:
            # print(v)
    
        for col in one_oil:
            answer[col] += count
    
    for row in range(len(land)):
        for col in range(len(land[0])):
            if not visited[row][col] and land[row][col] == 1:
                # print("new bfs starts with:",row,col)
                bfs(row, col, 1)
    
    return max(answer)