from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    want_discount = dict(zip(want, number))

    # 10일 할인을 받을 수 있는 범위에서 연속 할인 가능한지 확인
    for i in range(0,len(discount) - 9):
        temp_discount = defaultdict(int)

        for j in range(10):
            temp_discount[discount[i + j]] += 1
            # 10일 간 원하는 모든 제품을 할인 받을 수 없는 경우
            if discount[i + j] not in want_discount or temp_discount[discount[i + j]] > want_discount[discount[i+j]]: break
        # 원하는 모든 할인을 받을 수 있는 경우
        else:
            answer += 1

    return answer
