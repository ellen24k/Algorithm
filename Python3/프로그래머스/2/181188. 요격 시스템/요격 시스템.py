def solution(targets):
    s, e = 0, 0
    targets.sort()
    answer = 0
    
    for target in targets:
        s = max(s, target[0])
        e = min(e, target[1])
        if (e <= s): 
            answer += 1
            s, e = target
    return answer