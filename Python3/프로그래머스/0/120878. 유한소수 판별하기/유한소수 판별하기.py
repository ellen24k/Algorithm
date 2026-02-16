from fractions import Fraction

def solution(a, b):
    result = Fraction(a, b)
    c = result.denominator
    while (c % 2 == 0): c //= 2
    while (c % 5 == 0): c //= 5
    return 1 if c == 1 else 2