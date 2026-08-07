from collections import defaultdict

def solution(strArr):
    answer = defaultdict(int)
    for str_elem in strArr:
        answer[len(str_elem)] += 1
    return max(answer.values())