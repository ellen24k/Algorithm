def solution(q, r, code):
    answer = ''
    rIdx = r
    while(rIdx < len(code)):
        answer += code[rIdx]
        rIdx += q
    return answer