def solution(d, budget):
    d.sort()
    answer = 0

    for i in range(0,len(d)):
        budget -= d[i]
        if budget >= 0:
            answer += 1
        else:
            break;

    return answer 