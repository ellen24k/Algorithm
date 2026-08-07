def solution(n):
    if n < 3: return 1

    answer = 0
    seq_len = 1
    for i in range((n+1)//2):
        seq_num = n//seq_len + seq_len//2 # 해당 seq_len에서 연속될 수 있는 수의 최대값
        if seq_len > seq_num: return answer
    
        temp = 0
        for i in range(seq_len): # seq_len개의 연속된 자연수의 합
            temp += seq_num
            seq_num -= 1
        if temp == n: answer += 1
    
        seq_len += 1
    return answer