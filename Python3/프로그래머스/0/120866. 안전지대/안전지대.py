def solution(board):
    unsafe_set = set()
    n = len(board)
    answer = 0
    
    # 배열 순회하며 지뢰찾기
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            
            # 지뢰 찾으면 위험지역을 unsafe_set에 추가
            if col == 1:
                unsafe = (
                    (row_idx - 1, col_idx - 1), (row_idx - 1, col_idx), (row_idx - 1, col_idx + 1),
                    (row_idx, col_idx - 1), (row_idx, col_idx), (row_idx, col_idx + 1),
                    (row_idx + 1, col_idx - 1), (row_idx + 1, col_idx), (row_idx + 1, col_idx + 1)
                )
                for unsafe_point in unsafe:
                    if (0 <= unsafe_point[0] < n and 0 <= unsafe_point[1] < n):
                        unsafe_set.add(unsafe_point)

    # 전체 배열에서 위험지역 칸 수를 빼 안전지역 칸 수 구하기
    answer = n*n - len(unsafe_set)
    return answer