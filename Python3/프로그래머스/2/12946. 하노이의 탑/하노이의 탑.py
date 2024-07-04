def solution(n):
    answer = list(list())
    
    hanoi(n,answer,1,2,3)
    
    return answer;

def hanoi(n, answer,start,temp,to):
    if n == 1:
        answer.append([start,to])
    else:
        hanoi(n-1,answer,start,to,temp)
        answer.append([start,to])
        hanoi(n-1,answer,temp,start,to)