def solution(keyinput, board):
    w_end = (board[0] - 1) / 2
    h_end = (board[1] - 1) / 2
    
    coordinate = [0,0]
    for key in keyinput:
        if key == 'up' and coordinate[1] + 1 <= h_end: coordinate[1] = coordinate[1] + 1
        elif key == 'down' and coordinate[1] - 1 >= -h_end: coordinate[1] = coordinate[1] - 1
        elif key == 'left' and coordinate[0] - 1 >= -w_end: coordinate[0] = coordinate[0] - 1
        elif key == 'right' and coordinate[0] + 1 <= w_end: coordinate[0] = coordinate[0] + 1
    return coordinate