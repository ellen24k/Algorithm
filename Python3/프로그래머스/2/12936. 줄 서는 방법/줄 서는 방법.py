import math

def solution(n, k):
    num = [i for i in range(1, n + 1)]
    answer = []
    
    for i in range(n, 0, -1):
        fact_n = math.factorial(i - 1)
        num_idx = 0
        while (fact_n < k):
            k -= fact_n
            num_idx += 1
        answer.append(num[num_idx])
        del num[num_idx]
    
    return answer