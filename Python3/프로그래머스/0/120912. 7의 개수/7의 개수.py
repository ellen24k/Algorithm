def solution(array):
    answer = 0
    for elem in array:
        for chr in str(elem):
            if chr == '7':
                answer += 1
    return answer