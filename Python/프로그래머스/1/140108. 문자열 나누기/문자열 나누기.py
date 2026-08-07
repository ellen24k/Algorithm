from collections import defaultdict

def solution(s):
    answer = 0
    s_dict = defaultdict(int)
    first_char = s[0]
    for char in s:
        if len(s_dict) > 1 and sum(s_dict.values()) == 2*s_dict[first_char]:
            answer += 1
            first_char = char
            s_dict.clear()
        
        s_dict[char] += 1
    
    return answer + 1