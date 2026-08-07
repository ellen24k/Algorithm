from collections import Counter

def solution(participant, completion):
    part_cnt = Counter(participant)
    comp_cnt = Counter(completion)
    
    for part in part_cnt.items():
        if (part[0] not in comp_cnt or part[1] != comp_cnt[part[0]]):
            return part[0]