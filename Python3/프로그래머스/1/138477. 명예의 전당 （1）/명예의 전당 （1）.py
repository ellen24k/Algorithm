def solution(k, score):
    answer = list()
    cur_honors = list()
    
    for i in score:
        cur_honors.append(i)
        
        if(len(cur_honors) > k):
            cur_honors.remove(min(cur_honors))
            
        answer.append(min(cur_honors))
        
    return answer