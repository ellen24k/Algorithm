from collections import deque

def bfs(graph,n,m, visited):
    queue = deque([[0, 0]]) # [0,0],[1,1]
    visited[0][0] = 1
    
    x_weight = [0,1,0,-1] # 하->우->상->좌 순으로 이동하기 위한 가중치
    y_weight = [-1,0,1,0]
    
    while queue:
        [cur_x,cur_y] = queue.popleft()
        # print(cur_x, cur_y, graph[cur_x][cur_y]) # 주석처리
        for i in range(4):
            temp_x = cur_x + x_weight[i] # 이동하려는 좌표
            temp_y = cur_y + y_weight[i]
            
            if (temp_x>-1 and temp_x<n and temp_y>-1 and temp_y<m): # 맵 내부에 위치한 좌표인지 확인
                if graph[temp_x][temp_y] != 0: # 벽이 아닌지 확인
                    if not (visited[temp_x][temp_y]): # 지나간 적 없는 위치인지 확인
                        queue.append([temp_x,temp_y])
                        visited[temp_x][temp_y] = visited[cur_x][cur_y] + 1
                        if (visited[-1][-1] != 0) : # 상대 팀 진영에 도착 시 반복을 종료해 성능향상
                            queue.clear()
                            break
    
            # for r in visited: # 이동 경로 확인용
                # print(r)
            # print()
    
    return visited


def solution(maps):
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    # for r in visited: # 이동 경로 확인용
        # print(r) #
    # print() #
    count = bfs(maps, len(maps), len(maps[0]), visited)
    # print(count[-1][-1])
    return count[-1][-1] if count[-1][-1] else -1