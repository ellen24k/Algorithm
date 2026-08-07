def solution(s):
    answer = list()
    set_s = set()
    s = sorted(s[2:-2].split('},{'), key=lambda a: len(a))
    
    for i in s:
        temp = list(map(int, i.split(',')))
        
        for i in temp:
            if i not in set_s:
                answer.append(i)
        set_s.update(temp)
    
    return answer