def solution(score):
    rank = sorted([sum(s) for s in score], reverse = True)
    
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
            
    return [rankDict[sum(s)] for s in score]