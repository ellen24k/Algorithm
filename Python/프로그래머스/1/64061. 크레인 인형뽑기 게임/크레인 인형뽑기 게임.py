def solution(board, moves):
    answer = 0
    basket = []

    # 세로줄 가장 위의 인형 구하기
    def get_poppable_doll_of_col(col):
        for line in board:
            if line[col] != 0:
                top_doll = line[col]
                line[col] = 0
                return top_doll
        return None # 해당 줄이 모두 비어있으면 None 반환

    # 크레인 작업 시작
    for move in moves:
        doll = get_poppable_doll_of_col(move - 1)
        
        # 뽑은 인형이 없는 경우(빈 줄) 무시
        if doll is None:
            continue
            
        # 바구니가 비어있지 않고, 맨 위 인형과 일치하는 경우
        if basket and basket[-1] == doll:
            basket.pop() # 기존 인형 제거
            answer += 2  # 인형 2개가 사라지므로 +2
        else:
            basket.append(doll) # 바구니에 추가

    return answer
