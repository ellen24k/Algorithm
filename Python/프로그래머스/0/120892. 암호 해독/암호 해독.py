def solution(cipher, code):
    answer = [cipher[i] for i in range(code-1,len(cipher),code)]
    return ''.join(answer)