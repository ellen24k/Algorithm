def dfs(computers, row, col, visited):
    visited[col] = True
    # print(row) # network에 새로 연결된 노드 
    # print(visited) # 현재 visited 상태
    
    for new_node in range(len(computers)):
        # print([row,new_node])
        if computers[row][new_node] == 1: # 네트워크로 연결되어 있는가
            if visited[new_node] is False: # 이미 동일 네트워크에 연결되어 있는가
                dfs(computers,new_node,new_node,visited)
    

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)] # 컴퓨터별 방문 여부 -> [False, False, False]
    # for i in computers: # computer 확인
        # print(i) #
    # print() #
    
    for i in range(n):
        if visited[i] is False:
            # print("\nnew network") #네트워크별 연결된 컴퓨터 확인
            dfs(computers,i,i,visited)
            answer += 1
            
    return answer