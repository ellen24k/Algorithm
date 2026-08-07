def solution(phone_number):
    hide_num_len = len(phone_number) - 4
    return '*'*(hide_num_len) + phone_number[hide_num_len:]