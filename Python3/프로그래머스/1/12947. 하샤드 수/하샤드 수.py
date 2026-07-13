def solution(x):
    sum = 0
    str_x = str(x)
    
    for char_x in str_x:
        sum += int(char_x)
        
    return True if x % sum == 0 else False
