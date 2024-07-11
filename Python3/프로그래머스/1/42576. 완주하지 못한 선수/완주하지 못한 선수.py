from collections import Counter

def solution(participant, completion): # Counter 사용
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    
    return list(participant_counter - completion_counter)[0] # Counter끼리 빼기 가능


# def solution(participant, completion): # 단순 리스트 반복 -> 효율성 실패
#     for i in completion: 
#         if i in participant: participant.remove(i)
#     return answer