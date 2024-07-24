def solution(phone_book):
    phone_set = set(phone_book)
    
    for phone_num in phone_book:
        for i in range(1, len(phone_num)):
            if phone_num[:i] in phone_set:
                return False
    return True

# def solution(phone_book): # 효율성 시간초과
#     phone_book.sort(key=lambda x: len(x))
#     # print(phone_book)
    
#     for i in range(len(phone_book)-1):
#         for j in range(i+1, len(phone_book)):
#             # print("i:",phone_book[i],"j:",phone_book[j])
#             if phone_book[i] in phone_book[j][:len(phone_book[i])]:
#                 return False
    
#     return True