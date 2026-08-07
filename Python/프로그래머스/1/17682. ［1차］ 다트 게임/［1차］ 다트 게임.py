def solution(dartResult):
    answer = []
    length = len(dartResult)
    i = 0
    
    while(i < length):
        curVal = dartResult[i]
        
        if (curVal.isdigit()): 
            if (i + 1 < length and dartResult[i+1] == '0'): 
                curVal = '10'
                i += 1
            answer.append(int(curVal))
        elif (curVal == '*'):
            answer[-1] *= 2
            if (len(answer) > 1): answer[-2] *= 2
        elif (curVal == '#'): 
            answer[-1] *= -1
        else:
            if (curVal == 'D'): answer[-1] = pow(answer[-1],2)
            if (curVal == 'T'): answer[-1] = pow(answer[-1],3)
        i += 1
        # print(answer)
                
    return sum(answer)