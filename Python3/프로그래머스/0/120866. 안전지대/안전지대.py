def solution(board):
    answer = 0
    n = len(board)
    unsafe_set = set()
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if col == 1:
                unsafe = [
                    (row_idx - 1, col_idx - 1), (row_idx - 1, col_idx), (row_idx - 1, col_idx + 1),
                    (row_idx, col_idx - 1), (row_idx, col_idx), (row_idx, col_idx + 1),
                    (row_idx + 1, col_idx - 1), (row_idx + 1, col_idx), (row_idx + 1, col_idx + 1)
                ]
                for unsafe_point in unsafe:
                    if (0 <= unsafe_point[0] < n and 0 <= unsafe_point[1] < n):
                        unsafe_set.add(unsafe_point)
    answer = n*n - len(unsafe_set)
    return answer