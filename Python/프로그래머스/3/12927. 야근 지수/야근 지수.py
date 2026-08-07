def solution(n, works): # 성공
    answer = 0
    works.sort(reverse = True)
    # print(works)

    index = 0
    while(n > 0):
        if works[0] == 0: return 0
        while(works[index] == works[index+1]):
            index += 1
            if index == len(works) -1: break
        # print(n, index)

        works[index] -= 1
        n -= 1
        if index != 0: index -= 1

    for work in works:
        answer += work * work
        # print(work,end="")
    # print()
    return answer

# import heapq
# def solution(n, works): # 성공 but 느림 (최대 802.34ms)
#     answer = 0
#     work_heap = []
#     for work in works: # max heap
#         heapq.heappush(work_heap, (-work,work))
        
#     while(n > 0 and work_heap[0][1] != 0):
#         temp = heapq.heappop(work_heap)[1] - 1
#         heapq.heappush(work_heap, (-temp, temp))
#         n -= 1
        
    
#     for work in work_heap:
#         answer += work[1] * work[1]
#         # print(work,end="")
#     # print()
#     return answer
