def solution(n):
    converted = []
    while n > 0:
        n, mod = divmod(n, 3)
        if mod == 1: converted.append('1')
        elif mod == 2: converted.append('2')
        else : 
            converted.append('4')
            n -= 1 # 자릿수가 올라가는 문제
        # print(n, mod)
    return ''.join(reversed(converted))