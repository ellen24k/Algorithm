def solution(stones, k): # 이진탐색, 성공
    left = 1; mid = 0; right = max(stones)
    
    while(left <= right):
        mid = (left + right) // 2
        count = 0
        # print(left, mid, right, k)
        for stone in stones:
            if stone <= mid: 
                count += 1
                if count == k: break
            elif stone > mid:
                count = 0
            
        if count < k: left = mid + 1
        else: right = mid - 1
        # print("a:", left, mid, right, k, count)
    return left
                


# def solution(stones, k): # 효율성 전부 실패
#     max_between_k = [0 for _ in range(len(stones) - k + 1)]
    
#     for i in range(len(stones) - k + 1):
#         max_between_k[i] = max(stones[i : i + k])
#     # print(max_between_k)
#     return min(max_between_k)