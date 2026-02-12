from heapq import heappush, heappop

def solution(n, k, enemy):
    prev_n_min_heap = [] 
    round = 0
    
    for i in range(len(enemy)):
        heappush(prev_n_min_heap, enemy[i])
        if (k):
            round += 1
            k -= 1
        else:
            prev_min = heappop(prev_n_min_heap)
            if (n >= prev_min):
                round += 1
                n -= prev_min
            else: break

    return round