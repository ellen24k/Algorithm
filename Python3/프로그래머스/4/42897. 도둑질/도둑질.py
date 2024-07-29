def make_sum(last, money, with0):
    if with0: # 첫 번째 집 도둑질 여부로 케이스 나누기
        money[2] += money[0]
        money[3] += max(money[1], money[0])  
    else:
        money[3] += money[1]
        
    # money의 길이가 4 미만인 경우는 없음 (feat.solution)
    for i in range(4,last):
        money[i] += max(money[i - 2], money[i - 3])
        

def solution(money):
    if len(money) <= 3:
        return max(money)

    money1 = money.copy()
    money2 = money.copy()
            
    make_sum(len(money) - 1, money1, True) # 0번 집은 반드시 터는 경우
    make_sum(len(money), money2, False) # 0번 집을 빼고 터는 경우
    # print(money1, money2)
    return max(max(money1), max(money2))

# def solution(money): # 효율성 실패 > 재귀 한도 초과로 추정
#     if len(money) == 3:
#         return max(money)

#     money1 = money.copy()
#     money2 = money.copy()

#     def make_sum(cur, last, money, with0):
#         if cur > 3:
#             money[cur] += max(money[cur - 3: cur - 1])
#         else:
#             if with0: # 첫 번째 집 도둑질 여부로 케이스 나누기
#                 money[2] += money[0]
#                 money[3] += max(money[1], money[0])  
#             else:
#                 money[3] += money[1]
                
#         if cur < last:
#             make_sum(cur + 1, last, money, with0)
            
#     # cur >> money의 길이가 3 이하인 경우는 없음 (feat.solution)
#     make_sum(3, len(money) - 2, money1, True) # 0번 집은 반드시 터는 경우
#     make_sum(3, len(money) - 1, money2, False) # 0번 집을 빼고 터는 경우
#     # print(money1, money2)
#     return max(max(money1), max(money2))