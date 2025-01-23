def solution(s):
    answer = ''
    for char in set(s):
        if s.count(char) == 1: answer += char
    return ''.join(sorted(answer))