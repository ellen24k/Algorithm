def solution(s, n):
    answer = list(s)
    
    for i in range(0,len(answer)):
        cur_char = answer[i]
        
        if cur_char.isalpha():
            if cur_char.islower(): 
                answer[i] = chr(ord('a') + (ord(cur_char) - ord('a') + n) % 26)
            else: 
                answer[i] = chr(ord('A') + (ord(cur_char) - ord('A') + n) % 26)
            
    return ''.join(answer)