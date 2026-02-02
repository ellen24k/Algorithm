def solution(arr, queries):
    answer = []
    for query in queries:
        min = float('inf')
        for i in arr[query[0] : query[1] + 1]:
            if i > query[2] and i < min: min = i
        answer.append(min if min != float('inf') else -1)
    return answer