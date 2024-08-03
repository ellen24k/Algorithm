from itertools import combinations

def check_prime(num_list):
    prime_count = 0
    
    for num in num_list:
        num = sum(num)
        is_prime = True
        
        for i in range(2, int(num ** 0.5 +1)):
            if num % i == 0:
                is_prime = False
                break
        if is_prime: prime_count += 1

    return prime_count

def solution(nums):
    nCr = combinations(nums,3)
    return check_prime(list(nCr))