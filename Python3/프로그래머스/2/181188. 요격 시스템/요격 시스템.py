def solution(targets):
    s, e = 0, 0
    targets.sort(key=lambda x: x[1])
    answer = 0
    
    for target in targets:
        if (e <= target[0]): 
            answer += 1
            s, e = target
    return answer