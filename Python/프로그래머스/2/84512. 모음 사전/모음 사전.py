import itertools


def solution(word):
    answer = 0
    
    word_list = [] # 사전생성
    for i in range(1,6):
        word_list += list(itertools.product('AEIOU', repeat=i))
    word_list.sort()
    
    for word_candidate in word_list:
        answer += 1
        if ''.join(word_candidate) == word:
            return answer

    return -1