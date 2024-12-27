from collections import deque

def solution(queue1, queue2):
    goal_sum_of_q = (sum(queue1) + sum(queue2))/2
    
    queue = deque(queue1)
    queue2.reverse()
    
    cnt = 0
    cur_sum_q = sum(queue)
    while queue:
        if cur_sum_q == goal_sum_of_q: return cnt
        elif cur_sum_q < goal_sum_of_q: 
            if queue2: 
                queue.append(queue2.pop())
                cur_sum_q += queue[-1]
            else: return -1
        else:
            cur_sum_q -= queue.popleft()
        cnt += 1
    return -1