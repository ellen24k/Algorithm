def solution(numbers):
    answer = []
    
    for num in numbers: # f()에 대입할 숫자마다
        is_zero_converted_to_one = False
        binary_num_list = list(format(num, "b")) # 접두어 없이 이진수로 변환해 숫자 하나하나를 리스트의 원소로
        
        # print(num, binary_num_list)
        for i in range(len(binary_num_list)-1, -1, -1): # num의 작은 비트부터 탐색
            if binary_num_list[i] == '0':
                binary_num_list[i] = '1'
                is_zero_converted_to_one = True
                
                # 변환한 비트보다 작은 비트 중 1인 비트가 있다면 이 중 1개 비트를 0으로 바꿔주어야 x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수가 됨
                for j in range(i + 1, len(binary_num_list)): 
                    if binary_num_list[j] == '1':
                        binary_num_list[j] = '0'
                        break
                
                answer.append(int(''.join(binary_num_list), 2))
                break
            
        if is_zero_converted_to_one == False:
            answer.append(int('10' + '1'*(len(binary_num_list) - 1), 2))
            
        # print(answer)
    return answer