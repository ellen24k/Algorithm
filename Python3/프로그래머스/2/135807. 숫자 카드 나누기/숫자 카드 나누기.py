from math import gcd
from functools import reduce

def check_coprime(divisor, arr): # 서로소 확인
    for elem in arr:
        if not (elem % divisor): return False
    return True

def solution(arrayA, arrayB): # array가 정렬 되어있는 듯
    a_gcd = reduce(gcd, arrayA)
    b_gcd = reduce(gcd, arrayB)
    
    is_a_gcd_coprime_with_arrB = check_coprime(a_gcd, arrayB)
    is_b_gcd_coprime_with_arrA = check_coprime(b_gcd, arrayA)
    
    if is_a_gcd_coprime_with_arrB and is_b_gcd_coprime_with_arrA: return max(a_gcd, b_gcd)
    elif is_a_gcd_coprime_with_arrB: return a_gcd
    elif is_b_gcd_coprime_with_arrA: return b_gcd
    return 0