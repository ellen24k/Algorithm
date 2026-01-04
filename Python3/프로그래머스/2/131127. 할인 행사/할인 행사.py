from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    discount10days = defaultdict(int)
    wantDict = {want[i]: number[i] for i in range(len(want))}
    
    for i in range(9): discount10days[discount[i]] += 1
    
    for i in range(9, len(discount)):
        discount10days[discount[i]] += 1
        
        if (discount[i] in wantDict and discount10days[discount[i]] == wantDict[discount[i]]):
            # print(f'trigger: {discount[i]}')
            for k, v in wantDict.items():
                if (discount10days[k] != v): break
            else: answer += 1
            
        # print(discount10days)
        discount10days[discount[i - 9]] -= 1
    return answer