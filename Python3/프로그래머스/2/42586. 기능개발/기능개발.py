import math

def solution(progresses, speeds):
    answer = [1]
    releasable_date = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    
    pre_task = releasable_date[0]
    for i in releasable_date[1:]:
        if i > pre_task:
            pre_task = i
            answer.append(1)
        else: answer[-1] += 1
    
    # print(releasable_date)
    
    return answer