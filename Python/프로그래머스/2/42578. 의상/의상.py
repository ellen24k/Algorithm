def solution(clothes):
    clothes_by_type = {}
    answer = 1
    
    for c in clothes:
        if c[1] in clothes_by_type:
            clothes_by_type[c[1]].append(c[0])
        else:
            clothes_by_type[c[1]] = [c[0]]
    # print(clothes_by_type)
            
    for item in clothes_by_type.items():
        answer *= len(item[1]) + 1
        # print(item,answer)
    
    return answer - 1