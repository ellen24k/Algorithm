def solution(s):
    answer = list(s.upper())
    for i in range(0,len(answer)-1):
        if answer[i] != ' ':
            answer[i+1] = answer[i+1].lower()
    return ''.join(answer)