def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur_weight = 0
    queue = [0 for i in range(bridge_length)]
    
    while(len(queue) > 0):
        # print(weight, truck_weights, queue, cur_weight)
        answer += 1
        cur_weight -= queue.pop(0)
        
        if(len(truck_weights) > 0):
            if (cur_weight + truck_weights[0] <= weight):
                queue.append(truck_weights.pop(0))
                cur_weight += queue[-1]
            else:
                queue.append(0)
            
    
    return answer