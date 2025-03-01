def solution(s):
    answer = []
    separated_s = s.split()
    for separated in separated_s:
        if separated == 'Z': answer.pop()
        else: answer.append(int(separated))
    return sum(answer)