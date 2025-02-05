from collections import deque

def solution(x, y, n):
    if x == y: return 0

    q = deque([(y,0)])
    once_in_q = [y]
    
    while(q):
        num, operation_cnt = q.popleft()
        new_nums = (num / 3, num / 2, num - n)

        for new_num in new_nums:
            if new_num == x: return operation_cnt + 1
            if (new_num > x) and (new_num%1 == 0) and (new_num not in once_in_q): 
                q.append((new_num, operation_cnt + 1))
                once_in_q.append(new_num)
        
    return -1