def solution(sequence, k):
    answer = [0, len(sequence)]
    curSum = 0
    start = 0
    
    for i, val in enumerate(sequence):
        curSum += val
        
        while (curSum > k):
            curSum -= sequence[start]
            start += 1
        if (curSum == k and i - start < answer[1] - answer[0]):
            answer = [start, i]
            if (start == i): break
        
    return answer