def solution(n):
    origin_num = list(bin(n))
    answer = ''
    
    if origin_num.count('0') == 1: #'0bXXXX'이므로 기본적으로 0이 1개 존재
        answer = origin_num.insert(3,'0')
    else:
        switched = False
        for i in range(len(origin_num)-2,1,-1):
            
            if origin_num[i] == '0' and origin_num[i+1] == '1':
                
                origin_num[i], origin_num[i+1] = '1', '0'
                origin_num[i+1:] = sorted(origin_num[i+1:])
                switched = True
                break
                
        if not switched:
            # print(origin_num,type(origin_num))
            origin_num.insert(3,'0')
            origin_num[3:] = sorted(origin_num[3:])
                

        
    answer = ''.join(origin_num)
    answer = int(answer,2) #2진수 -> 10진수로 변환
    # print(answer,type(answer))
    return answer