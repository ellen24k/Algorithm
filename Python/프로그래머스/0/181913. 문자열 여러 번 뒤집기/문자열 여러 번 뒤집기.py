def solution(my_string, queries):
    answer = [char for char in my_string]
    
    for query in queries:
        s,e = query
        while (s < e):
            answer[s], answer[e] = answer[e], answer[s]
            s += 1
            e -= 1
        
    return ''.join(answer)