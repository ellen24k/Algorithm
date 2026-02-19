def solution(n, cores):
    answer = 0
    left, right = 0, min(cores) * n
    
    while (left <= right):
        mid = (left + right) // 2
        # mid 시점에 완료된 작업 수
        done_works = sum((mid // core) + 1 for core in cores) 
        
        if (done_works < n): left = mid + 1
        else: right = mid - 1 
    
    # left = 완료된 작업 >= n인 최소 시점
    done = sum(((left - 1) // core) + 1 for core in cores)  

    for i, core in enumerate(cores):
        if left % core == 0:
            done += 1
            if done == n: return i + 1

    return answer