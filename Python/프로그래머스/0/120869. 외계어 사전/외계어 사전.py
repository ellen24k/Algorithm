def solution(spell, dic):
    for di in dic:
        valid = True
        
        for sp in spell:
            if di.count(sp) != 1:
                valid = False
                break
        
        if valid: return 1
        
    return 2