def solution(land):

    for i in range(1,len(land)):
        for j in range(4):
            land[i][j] += max(land[i -1][: j] + land[i - 1][j + 1:])
            # land[i][j] += max((land[i-1][index] for index in range(4) if index != j))
        # print(i,land[i])
        
    return max(land[-1])