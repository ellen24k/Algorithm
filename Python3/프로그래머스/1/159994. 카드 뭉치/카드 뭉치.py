def solution(cards1, cards2, goal):
    cards1.append('')
    cards2.append('')
    i1 = i2 = 0
    
    for i in range(len(goal)):
        # print(goal[i],cards1[i1],cards2[i2])
        if goal[i] == cards1[i1]:
            i1 += 1
        elif goal[i] == cards2[i2]:
            i2 += 1
        else: return "No"
    
    return "Yes"