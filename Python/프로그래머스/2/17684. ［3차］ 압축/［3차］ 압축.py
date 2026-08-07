def solution(msg):
    answer = []
    last_num = 1
    LZW_dict = {}
    
    # 길이가 1인 모든 단어를 포함하도록 사전을 초기화
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        LZW_dict[c] = last_num
        last_num += 1
    # print(LZW_dict)
    
    start_idx = 0
    while start_idx < len(msg):
        last_idx = start_idx + 1
        # 사전에서 현재 입력과 일치하는 가장 긴 문자열 찾기
        while last_idx <= len(msg) and msg[start_idx:last_idx] in LZW_dict:
            last_idx += 1
        
        # 입력과 일치하는 가장 긴 문자열 색인 번호를 출력
        answer.append(LZW_dict[msg[start_idx:last_idx - 1]])
        # 입력에서 처리되지 않은 다음 글자가 남아있다면 해당 단어를 사전에 등록
        if last_idx <= len(msg): 
            LZW_dict[msg[start_idx:last_idx]] = last_num
            last_num += 1
        start_idx = last_idx - 1
        # print(f'append: {answer[-1]}')
            
    return answer