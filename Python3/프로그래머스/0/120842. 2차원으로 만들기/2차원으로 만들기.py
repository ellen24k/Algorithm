def solution(num_list, n):
    answer = []
    num_list.reverse()
    while num_list:
        temp = []
        for i in range(n): 
            if num_list: 
                temp.append(num_list.pop())
        answer.append(temp)
    return answer