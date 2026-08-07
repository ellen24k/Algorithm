def solution(n):
    answer = []
    for char in reversed(str(n)):
        answer.append(int(char))
    return answer