def solution(l, r):
    answer = []
    l_5 = ((l+4) // 5) * 5
    
    for i in range(l_5, r + 1, 5):
        is_05 = True
        for char in str(i):
            if char not in '05': 
                is_05 = False
                break
        if is_05: answer.append(i)
    return answer if len(answer) != 0 else [-1]