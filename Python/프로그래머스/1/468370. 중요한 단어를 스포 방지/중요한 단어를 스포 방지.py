def solution(message, spoiler_ranges):
    not_important = set()
    important = set()
    
    word_start = 0
    idx = 0
    
    # 전체 message 순회
    while idx < len(message):
        # idx 정보를 유지하며 ' ' 기준 단어 split
        while idx < len(message) and message[idx] != ' ':
            idx += 1
        
        # spoiler 범위에 있는지 확인 후 메세지 분류
        is_not_important = True
        for spoiler_range in spoiler_ranges:
            # spoiler 범위가 단어 이전이면 continue
            if spoiler_range[1] < word_start:
                continue
            # spoiler 범위에 단어가 포함되면 import 단어에 추가
            elif word_start <= spoiler_range[1] and idx - 1 >= spoiler_range[0]:
                is_not_important = False
                important.add(message[word_start: idx])
            # spoiler 범위가 단어 이후라면 다음 범위 비교 필요없음
            elif spoiler_range[0] > idx:
                break
                
        if is_not_important:
            not_important.add(message[word_start: idx])
        # print(word_start, idx, message[word_start:idx])
        word_start = idx + 1
        idx += 1
        
    # print("important:", important)
    # print("not important:", not_important)
    
    # 메시지의 스포 방지 구간이 아닌 구간에 등장한 적 없는 중요 단어 반환
    return len(important - not_important)