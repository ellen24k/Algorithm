def solution(common):
    if common[1] - common[0] == common[2] - common[1]: # 등차
        return common[-1] + (common[1] - common[0])
    else: # 등비
        return common[-1] * (common[1] // common[0])
