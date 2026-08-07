import heapq

def solution(scoville, K): # min heap으로 시도 -> 성공
    heapq.heapify(scoville) # 리스트를 min heap으로 변환
    answer = 0
    
    for i in range(len(scoville) - 1):
        if(scoville[0] >= K): break # 루트 노드 인덱스 = 0 -> 최솟값
        most_min = heapq.heappop(scoville) # 힙의 최솟값 pop
        secondary_min = heapq.heappop(scoville)
        heapq.heappush(scoville, most_min + secondary_min*2)
        answer += 1
        
    return answer if scoville[-1] >= K else -1

# def solution(scoville, K): # 정렬로 시도 -> 효율성 시간 초과
#     scoville.sort(reverse=True)
#     answer = 0
#     max_ans = len(scoville) - 1
    
#     while(answer < max_ans):
#         if(scoville[-1] >= K): break
        
#         scoville[-2] = scoville[-2] * 2 + scoville[-1]
#         scoville.pop()
#         scoville.sort(reverse=True)
#         answer += 1
        
        
#     return answer if scoville[-1] >= K else -1