def solution(priorities, location):
    answer = 0
    cur_location = location
    priority_based_list = sorted(priorities, reverse=True)
    
    for pre_task in priority_based_list:
        while(priorities[0] != pre_task) :
            
            cur_location = cur_location = len(priorities) - 1 if cur_location == 0 else cur_location - 1
            priorities.append(priorities.pop(0))
            
        # print(cur_location, pre_task, priorities, priority_based_list)
        answer += 1
        if cur_location == 0: return answer
        else: 
            cur_location -= 1
            priorities.pop(0)


# def solution(priorities, location): # 문제 이해 잘못함, 큐에 들어간 순서를 무조건 유지함
#     list_with_index = [[l,p] for l,p in enumerate(priorities)] # [location, priotity]
#     list_with_index.sort(key=lambda x: (-x[1], x[0])) # 튜플로 정렬 기준 복수 개 설정 가능
#     print(list_with_index)

#     return list_with_index.index([location, priorities[location]]) + 1