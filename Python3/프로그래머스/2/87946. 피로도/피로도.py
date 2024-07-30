def solution(k, dungeons):
    answer = 0
    dungeons.sort(key=lambda x : -(x[0]-x[1]))
    visited = [0 for _ in range(len(dungeons))]
    # print(dungeons); print(visited)
    
    
    def dfs(remain_k, index, count):
        nonlocal answer
        visited[index] = count
        # print(visited, count, remain_k, index)
        
        if 0 in visited:
            for i in range(len(dungeons)):
                if visited[i] == 0 and remain_k >= dungeons[i][0]:
                    dfs(remain_k - dungeons[i][1], i, count + 1)
        
        answer = max(answer, max(visited))
        if 0 in visited: visited[index] = 0; 
    
    for i in range(len(dungeons)):
        # print("for:",i, answer)
        dfs(k - dungeons[i][1],i,1)
        if answer == len(dungeons): break
    return answer