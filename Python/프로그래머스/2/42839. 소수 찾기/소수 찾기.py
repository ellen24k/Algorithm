import itertools

def is_prime_num(n): # 소수판별
    if n < 2: return False

    for i in range(2, int(n ** 0.5 +1)): # 제곱근을 기준으로 약수의 개수는 대칭
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    s = set()
    
    for i in range(1, len(numbers) + 1): # 종이를 붙이는 순열(순서를 고려한 나열)
        temp = list(itertools.permutations(numbers,i))
        # print("temp",temp)
        for j in temp:
            s.add(int(''.join(j)))
    
    # print(s)
    for i in list(s): # 소수 개수 확인
        if is_prime_num(i):
            # print("prime:",i)
            answer += 1
    
    return answer

