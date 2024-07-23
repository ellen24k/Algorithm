import heapq

def solution(operations):
    heap = []
    
    for operation in operations:
        if operation[0] == "I":
            heapq.heappush(heap,int(operation[2:]))
        elif len(heap) > 0:
            # print("operation:",operation)
            if operation == "D 1": # 최댓값 삭제
                heap.remove(heapq.nlargest(1, heap)[0])
            else:
                heapq.heappop(heap) # 최솟값 삭제
        # print(heap)
            
    if len(heap) > 0 : return [heapq.nlargest(1,heap)[0],heap[0]]
    else: return [0,0]