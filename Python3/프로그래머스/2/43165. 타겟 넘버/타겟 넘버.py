from collections import deque

def bfs(graph, length, target):
    queue = deque([[0,graph[0]],[0,-graph[0]]]) # [[index, value], [index, value], [index, value], ...]
    method_count = 0
    
    while(queue):
        [index,value] = queue.popleft() # [0,1] -> index = 0, value = 1
        
        if index + 1 < length: # 아직 graph에 계산해야 할 원소가 남아있는 경우
            queue.append([index+1, value+graph[index+1]])
            queue.append([index+1, value-graph[index+1]])
        elif value == target: method_count += 1 # 계산해야 할 원소가 없는 경우 value가 target이면 주어진 숫자를 만드는 방법
        # print(queue)
        
    return method_count
        
        


def solution(numbers, target):
    answer = bfs(numbers,len(numbers),target)
    # print(answer)
    return answer