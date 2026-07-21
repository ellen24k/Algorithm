def solution(picks, minerals):
    answer = 0
    stresses = []
    
    # 최대 채굴 가능 광물량만 계산
    if len(minerals) > 5*sum(picks):
        minerals = minerals[:5*sum(picks)]
        
    # 피로도에 따른 레벨 부여
    mineral_level = {'diamond': 'a', 'iron': 'b', 'stone': 'c'}
    
    # 곡괭이별 피로도 {pick: (diamond 피로도, iron 피로도, stone 피로도)}
    pick_level = {
        0: {'a': 1, 'b': 1, 'c': 1}, # diamond
        1: {'a': 5, 'b': 1, 'c': 1}, # iron
        2: {'a': 25, 'b': 5, 'c': 1}, # stone
    }
    
    # 연속 채굴하는 광물 단위로 피로도 높은 순서에 따라 분류
    chunk = []
    chunk_cnt = 0
    for mineral in minerals:
        chunk.append(mineral_level[mineral])
        chunk_cnt += 1
        if chunk_cnt == 5:
            stresses.append(''.join(sorted(chunk)))
            chunk = []
            chunk_cnt = 0
    if chunk_cnt:
            stresses.append(''.join(sorted(chunk)))
    # 광물 채굴에 요구되는 피로도가 높고 광물량이 많은 순서대로 chunk의 피로도가 높음
    stresses.sort(key = lambda x: (x, -len(x))) 
    
    # 피로도 높은 광물을 좋은 곡괭이로 채굴
    stress_idx = 0
    for pick_idx in range(len(picks)):
        # 해당 pick_level의 곡괭이 사용 가능한지 확인
        for pick in range(picks[pick_idx]):
            for char in stresses[stress_idx]:
                answer += pick_level[pick_idx][char]
            if stress_idx < len(stresses) - 1: 
                stress_idx += 1 
            else: # 광물 총량 < 사용 가능한 곡괭이 수
                return answer
