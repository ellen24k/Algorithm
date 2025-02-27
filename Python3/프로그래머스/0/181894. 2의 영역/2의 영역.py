def solution(arr):
    start_idx = -1
    last_idx = -1
    
    for i, num in enumerate(arr):
        if num == 2:
            if start_idx == -1: start_idx = i
            last_idx = i

    return arr[start_idx: last_idx + 1] if start_idx != -1 else [-1]