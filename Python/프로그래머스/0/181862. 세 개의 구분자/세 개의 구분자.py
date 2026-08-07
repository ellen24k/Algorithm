def solution(myStr):
    ans = [i for i in myStr.replace('b', 'a').replace('c', 'a').split('a') if i]
    return ans if ans else ["EMPTY"]