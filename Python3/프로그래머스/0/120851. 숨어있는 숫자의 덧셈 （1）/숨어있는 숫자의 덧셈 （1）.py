def solution(my_string):
    str_list = list(my_string)
    answer = 0
    for i in str_list:
        if i.isalpha() == False:
            answer += int(i)
    return answer