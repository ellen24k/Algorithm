def solution(number, limit, power):
    divisor_list = [get_divisor(num,limit,power) for num in range(1,number+1)]
    # print(divisor_list)
    return sum(divisor_list)

def get_divisor(num,limit,power):
    count = 0
    for i in range(1,int(num**(1/2))+1):
        
        if num%i==0: 
            if i==num**(1/2): count += 1
            else: count += 2
            
        if count > limit:
            count = power
            break
            
    return count