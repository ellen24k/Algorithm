def solution(quiz):
    answer = []
    
    for q in quiz:
        L, R = q.split(' = ')
        X, op, Y = L.split()
        
        if op == '+': result = 'O' if int(X) + int(Y) == int(R) else 'X'
        else: result = 'O' if int(X) - int(Y) == int(R) else 'X'
        
        answer.append(result)
            
    return answer