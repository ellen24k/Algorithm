def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            answer.extend([arr[i]]*arr[i]*2)
        else:
            cnt = arr[i]
            for i in range(cnt):
                answer.pop()
    return answer