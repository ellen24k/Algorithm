import re

def solution(my_string):
    answer = 0
    temp = re.split('[A-Za-z]', my_string)
    for i in temp:
        if i.isdigit(): answer += int(i)
    return answer