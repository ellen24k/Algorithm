def solution(arr):
    new_len = 1
    origin_len = len(arr)
    while origin_len > 1:
        origin_len /= 2
        new_len *= 2
    answer = arr.copy()
    while (len(answer) < new_len): answer.append(0)
    return answer