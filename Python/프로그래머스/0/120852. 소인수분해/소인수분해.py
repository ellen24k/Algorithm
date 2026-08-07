def solution(n):
    answer = []
    if (n % 2 == 0):
        while (n % 2 == 0):
            n /= 2  
        answer.append(2)
    
    prime = 3
    while (n > 2 and n >= prime):
        if (n % prime == 0):
            while (n % prime == 0):
                n /= prime
            answer.append(prime)
        prime += 2
    return answer