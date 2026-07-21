def solution(s, skip, index):
    answer = []
    invalid_char = set(skip) # skip할 char
    
    for char in s:
        cnt = 0
        while cnt < index: # skip을 제외하고 index만큼 뒤에 있는 알파벳 추가
            char = chr(ord(char) + 1) if char != 'z' else 'a'
            if char not in invalid_char: # 유효한 char라면 index cnt 증가
                cnt += 1
        answer.append(char)
    return ''.join(answer)