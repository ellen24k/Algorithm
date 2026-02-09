def solution(common):
    d = common[1] - common[0]
    r = common[1] // common[0] if common[0] != 0 else 0
    if (common[-1] - common[-2] == d): return common[-1] + d
    else: return common[-1] * r