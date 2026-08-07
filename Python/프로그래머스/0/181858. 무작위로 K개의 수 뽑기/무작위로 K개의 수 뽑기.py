def solution(arr, k):
    answer = [-1]*k
    i = 0
    
    for elem in arr:
        if (elem not in answer):
            answer[i] = elem
            i += 1
        if (i >= k): break
    
    return answer