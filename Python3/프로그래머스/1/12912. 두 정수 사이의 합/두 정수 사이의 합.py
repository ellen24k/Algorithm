def solution(a, b):
    min, max = sorted([a,b])
    # print(min, max)
    answer = sum(range(min, max + 1))
    return answer