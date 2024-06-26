def solution(price):
    answer = 0
    
    if price < 100_000:
        answer = price
    elif price < 300_000:
        answer = price * 0.95
    elif price < 500000:
        answer = price * 0.9
    else:
        answer = price * 0.8
    
    
    return int(answer)