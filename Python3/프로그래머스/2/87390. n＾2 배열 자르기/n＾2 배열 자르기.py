def solution(n, left, right):
    answer = make_table(n,left,right)
    return answer

def make_table(n,left,right):
    table = [0 for i in range(right - left + 1)]
    
    real_index = left
    row_weight = real_index//n + 1
    
    for index in range(len(table)):
        table[index] = max(real_index%n + 1, row_weight)
        
        real_index += 1
        if real_index % n == 0: row_weight += 1
        
    return table


# def solution(n, left, right):
#     answer = make_table(n)
#     return answer[left:right + 1]

# def make_table(n): # 1차원 배열 전체 [1~n] * n 초기화 후 특정 인덱스의 값 수정 -> 시간초과 + 런타임 에러
    # table = [i+1 for i in range(n)] * n
    
    # for i in range(n):
        # for j in range(i):
            # table[n*i + j] = i + 1
    
    # print(table)
    # return table       

# def make_table(n): # 시도1: 2차원 배열로 해결 -> 시간 초과
#     table =  [[0 for j in range(n)] for i in range(n)]
    
#     for key,value in enumerate(table):
#         count = key + 1
        
#         for index in range(len(value)):
#             if count > 0:
#                 value[index] = key + 1
#                 count -= 1
#             else:
#                 value[index] = index + 1
#         # print(key,value)
        
#     return sum(table,[]) #2차원 리스트 1차원으로 변환
