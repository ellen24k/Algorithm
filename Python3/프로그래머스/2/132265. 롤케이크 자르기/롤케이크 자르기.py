from collections import defaultdict

def solution(topping):
    answer = 0
    toppingTypesForOlder = set(topping)
    toppingCntForOlder = defaultdict(int)
    for top in topping: toppingCntForOlder[top] += 1
        
    toppingTypesForYounger = set()
    toppingCntForYounger = defaultdict(int)
    
    for top in topping:
        toppingCntForOlder[top] -= 1
        if (toppingCntForOlder[top] == 0): toppingTypesForOlder.remove(top)
        
        toppingCntForYounger[top] += 1
        if (toppingCntForYounger[top] == 1): toppingTypesForYounger.add(top)
        
        if (len(toppingTypesForOlder) == len(toppingTypesForYounger)): answer += 1
    return answer