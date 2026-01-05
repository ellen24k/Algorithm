# https://school.programmers.co.kr/learn/courses/30/lessons/181830
def solution(arr):
    answer = arr
    
    rowLen = len(arr)
    colLen = len(arr[0])
    
    if (rowLen > colLen):
        diff = rowLen - colLen
        for row in answer:
            row.extend([0 for _ in range(diff)])
    elif (colLen > rowLen):
        diff = colLen - rowLen
        for i in range(diff):
            answer.append([0 for _ in range(colLen)])
    return answer
