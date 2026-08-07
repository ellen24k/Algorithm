def solution(numbers, hand):
    answer = []
    coordinate = {i: ((i-1)//3, (i-1)%3) for i in range(1,10)}
    coordinate[0] = (3,1)
    coorL = (3,0)
    coorR = (3,2)
    
    for num in numbers:
        if (num in (1,4,7)): answer.append('L')
        elif (num in (3,6,9)): answer.append('R')
        else:       
            distL = abs(coordinate[num][0] - coorL[0]) + abs(coordinate[num][1] - coorL[1])
            distR = abs(coordinate[num][0] - coorR[0]) + abs(coordinate[num][1] - coorR[1])
            if (hand == 'right'): answer.append('R' if distR <= distL else 'L')
            else: answer.append('R' if distR < distL else 'L')
        
        if (answer[-1] == 'R'): coorR = coordinate[num]
        else: coorL = coordinate[num]
    return ''.join(answer)