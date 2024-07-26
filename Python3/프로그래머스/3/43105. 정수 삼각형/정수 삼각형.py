def solution(triangle):
        
    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])):
            # print(triangle[row][col])
            if col == 0:
                triangle[row][col] += triangle[row-1][0]
            elif col == row:
                triangle[row][col] += triangle[row-1][row-1]
            else:
                triangle[row][col] += max(triangle[row-1][col-1], triangle[row-1][col])
            # print(triangle[row][col])
                
    # for i in triangle:
        # print(i)
        
    return max(triangle[-1])


# import heapq

# def solution(triangle): # 시간초과
#     sum_max = []
    
#     def dfs(triangle, index_r, index_c, cur_sum):
#         cur_sum += triangle[index_r][index_c]
    
#         if index_r + 1 < len(triangle):
#                 dfs(triangle, index_r + 1, index_c, cur_sum),
#                 dfs(triangle, index_r + 1, index_c + 1, cur_sum)
#         else: heapq.heappush(sum_max,(-cur_sum, cur_sum))
    
#     dfs(triangle, 0,0,0)
    
#     return sum_max[0][1]