def solution(N, number):
    if N == number: return 1
    dp = {i: {int(str(N) * i)} for i in range(1,9)} # {N 사용 횟수 i번: i개의 N으로 만들 수 있는 숫자 set}
    # print(dp)

    for i in range(2,9):
        if number in dp[i]: return i
    
        for k in range(1, i//2 + 1):
            # print(f'i: {i} k: {k}')
            
            for val1 in dp[i - k]:
                for val2 in dp[k]:
                    if val1 == 0 or val2 == 0: continue
                    
                    # print(f'val1: {val1} val2: {val2}')
                    temp = {val1 + val2, abs(val1 - val2), val1*val2, val2 // val1 if val2 > val1 else val1 // val2}
                    
                    if number in temp: return i
                    else:
                        for temp_val in temp:
                            if temp_val not in dp[i - k] and temp_val not in dp[k]:
                                dp[i].add(temp_val)
            # print(i, dp[i], '\n')
    return -1