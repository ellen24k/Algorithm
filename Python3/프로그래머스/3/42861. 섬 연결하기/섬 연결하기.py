from collections import defaultdict

def is_connected(linked, node):
    # print(linked, 'connection check:', node)
    start, end = node[0], node[1]
    visited = set()
    stack = [start]
    
    while (stack):
        cur_node = stack.pop()
        if cur_node == end:
            return True
        if cur_node not in visited:
            visited.add(cur_node)
            stack.extend(linked[cur_node])
        # print('s:', stack, 'v:', visited)
        
    return False

def solution(n, costs):
    linked = defaultdict(set)
    costs.sort(key=lambda x: (x[2], x[0]))
    answer = 0
    # print(costs)
    
    for cost in costs:
        if cost[0] not in linked or cost[1] not in linked or not is_connected(linked, cost):
            linked[cost[0]].add(cost[1])
            linked[cost[1]].add(cost[0])
            answer += cost[2]
    # print(linked)
    
    return answer     