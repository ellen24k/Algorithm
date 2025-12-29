def solution(arr, queries):
    answer = arr
    for query in queries:
        s,e,k = query
        # print(s,e,k)
        for j in range(s,e+1):
            if (j%k == 0): 
                answer[j] += 1
    return answer