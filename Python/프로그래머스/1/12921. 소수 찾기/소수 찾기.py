def solution(n): # 에라스토테네스의 체
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)



# def prime_count(num): # 성공
#     count = 0
#     for i in range(2,num + 1):
#         is_prime = True
#         for j in range(2,int(i**0.5) + 1):
#             if i%j == 0:
#                 is_prime = False
#                 break
#         if is_prime: count += 1
#     return count

# def solution(n):
#     return prime_count(n)