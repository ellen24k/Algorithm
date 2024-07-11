from collections import Counter

def solution(participant, completion):
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    
    temp = list(participant_counter - completion_counter)
    return temp[0]


# def solution(participant, completion): # 단순 리스트 반복 -> 효율성 실패
#     for i in completion: 
#         if i in participant: participant.remove(i)
#     return answer