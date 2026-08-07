def dfs(tickets, index, order, visited):
    visited[index] = order
    # print(visited)

    for new_index in range(len(tickets)):
        # print(
        #     "n:",new_index,"->",tickets[new_index][0],
        #     "|i:",index,"->",tickets[index][1],
        #     "/o:",order
        # )

        if(tickets[index][1] == tickets[new_index][0]): # 도착지 == 출발지
            if visited[new_index] == 0: # 사용하지 않은 티켓
                # print(tickets[index],tickets[new_index])
                dfs(tickets,new_index,order+1,visited) # order + 1 -> 다음 방문지
                
    if(0 in visited): visited[index] = 0
    return visited


def solution(tickets):
    answer = ["ICN"]
    tickets.sort(key=lambda x: x[1])
    # print(tickets)

    for i in range(len(tickets)):
        if tickets[i][0] == "ICN": # 여행 시작지
            used = [0 for _ in range(len(tickets))] # 초기화된 티켓 사용여부
            order = dfs(tickets,i,1,used)
            # print("used:",used)
            if 0 not in order: # 모든 도시 방문
                order_dict = {order[i]: i for i in range(len(order))}
                # order_dict = {value: index for index, value in enumerate(order)}
                # print("ord_dic:",order_dict)

                temp = [tickets[order_dict[i+1]][1] for i in range(len(tickets))]
                answer += temp
                print(answer)
                return answer

    return 0