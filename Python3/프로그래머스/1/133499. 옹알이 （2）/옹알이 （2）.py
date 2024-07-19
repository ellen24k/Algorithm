import re

def solution(babbling):
    answer = 0
    reg = re.compile('^(aya|ye|woo|ma)+$') # 정규식을 컴파일해 패턴 생성
    sayable = ["aya","ye","woo","ma"]
    
    for babble in babbling: #["aya", "yee", "u", "maa"]
        if (
                reg.match(babble) and 
                not any(babble.count(saying*2) > 0 for saying in sayable)
            ):
            answer += 1
            # print(babble)
    return answer