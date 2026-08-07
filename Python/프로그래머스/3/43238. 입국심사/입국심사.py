def solution(n, times):
    left = 1
    right = max(times)*n
    mid = 0
    
    while(left <= right):
        mid = (left + right) // 2
        count = 0
        for time in times:
            count += mid//time
            if count >= n: break
        if count >= n: right = mid - 1
        else: left = mid + 1
        # print(left, mid, right, count)    
    
    return left