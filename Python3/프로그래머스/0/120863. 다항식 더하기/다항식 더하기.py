def solution(polynomial):
    number = 0
    x = 0
    
    for char in polynomial.split(" + "):
        if (char.isnumeric()): number += int(char)
        else: x += int(char[:-1] or "1")
        
    if (x > 0): 
        if (number > 0): return f"{x if x > 1 else ''}x + {number}"
        return f"{x if x > 1 else ''}x"
    return f"{number}"