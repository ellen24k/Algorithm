from collections import defaultdict
import sys
sys.setrecursionlimit(10000) # 재귀 한도 임의 지정, 기본 1000


def get_assignable_room_num(assigned_rooms, room_number):  # 배정 가능한 빈 방 번호 찾기
    if room_number not in assigned_rooms:
        assigned_rooms[room_number] = room_number + 1 # 빈 방의 다음 방
        return room_number
    
    next_empty_room = get_assignable_room_num(assigned_rooms, assigned_rooms[room_number])
    assigned_rooms[room_number] = next_empty_room + 1
    return next_empty_room



def solution(k, room_numbers):  # 3차 시도, 방 할당 시 배정 가능한 다음 빈 방 번호를 함께 저장
    room_num_len = len(room_numbers)
    answer = [0] * room_num_len
    assigned_rooms = defaultdict(int)  # {방 번호: 다음 빈 방 번호}

    for i in range(room_num_len):
        answer[i] = get_assignable_room_num(assigned_rooms, room_numbers[i])

    return answer


# def solution(k, room_numbers): # 2차 시도, 실패, 효율성 전부 시간초과
#     answer = []
#     assigned_rooms = set()
    
#     def assign_rooms(room_number):
#         for new_room_num in range(room_number,k + 1):
#             if new_room_num not in assigned_rooms:
#                 assigned_rooms.add(new_room_num)
#                 return new_room_num   
#     #
#     for i in range(len(room_numbers)):
#         answer.append(assign_rooms(room_numbers[i]))

#     return answer


# def solution(k, room_numbers): # 1차시도, 실패, 효율성 전부 런타임에러 -> 재귀 깊이 한도 초과로 추정
#     answer = []
#     assigned_rooms = set()
    
#     def assign_rooms(room_number):
#         assigned_room = -1
#         if room_number in assigned_rooms:
#             assigned_room = assign_rooms(room_number + 1)
#         else:
#             assigned_room = room_number
#             assigned_rooms.add(room_number)
#         return assigned_room    
    
#     for i in range(len(room_numbers)):
#         answer.append(assign_rooms( room_numbers[i]))

#     return answer