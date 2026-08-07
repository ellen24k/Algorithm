def solution(s):
    
    answer = sorted(map(int,s.split()))
    return "{0} {1}".format(answer[0], answer[-1]);