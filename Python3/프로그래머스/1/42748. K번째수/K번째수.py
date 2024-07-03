def solution(array, commands):
    answer = []
    
    for l in commands:
        answer.append(sorted(array[l[0]-1:l[1]])[l[2]-1])
        
    return answer