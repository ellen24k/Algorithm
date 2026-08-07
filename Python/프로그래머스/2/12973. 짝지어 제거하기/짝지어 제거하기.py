def solution(s):
    
    stack = list()
    
    for s_char in s:
        stack.append(s_char)
        
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            del stack[-2:]
            
    return 1 if not len(stack) else 0
        