from collections import deque

def solution(board, h, w):
    count = 0
    
    weight = ((1,0), (0,1), (-1,0), (0,-1)) # row, col

    for i in range(4):
        new_r = h + weight[i][0]
        new_c = w + weight[i][1]
        if new_r >= 0 and new_c >= 0 and new_r < len(board) and new_c < len(board[0]):
            if board[new_r][new_c] == board[h][w]:
                    count += 1
            # print(queue)
    return count