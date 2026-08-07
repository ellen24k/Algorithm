def solution(n, m):
    if n == m: # 두 수가 같을 때, 최소공배수 = 최대공약수
        return [n,m]

    #두 수의 소인수 리스트 구하기
    n_divisors = get_divisors(n)
    m_divisors = get_divisors(m)
    
    # 약수 비교해서 공약수 공배수 구하기
    greatest_common_denominator = 1 # 최대공약수
    least_common_multiple = 1 # 최소공배수
    
    n_index = m_index = 0
    while(len(n_divisors) > n_index or len(m_divisors) > m_index):
        
        # n(m)의 모든 소인수 처리 완료 시 m(n)에 남아있는 모든 인수를 최소공배수에 곱하기
        if(len(n_divisors) == n_index):
            for i in range(m_index,len(m_divisors)):
                least_common_multiple *= m_divisors[m_index]
                m_index += 1
            break;
            
        elif(len(m_divisors) == m_index):
            for i in range(n_index,len(n_divisors)):
                least_common_multiple *= n_divisors[n_index]
                n_index += 1
            break;
        
        # n과 m의 소인수가 같으면 공약수
        if(n_divisors[n_index] == m_divisors[m_index]):
            print("{} {}".format(n_divisors[n_index], m_divisors[m_index]))
            greatest_common_denominator *= n_divisors[n_index]
            n_index +=1
            m_index +=1
        
        # n과 m의 소인수가 같지 않으면 해당 소인수는 최소공배수에 곱하기
        elif(n_divisors[n_index] >= m_divisors[m_index]):
            least_common_multiple *= m_divisors[m_index]
            m_index += 1
            
        else:
            least_common_multiple *= n_divisors[n_index]
            n_index += 1
    
    #최소공배수 = 최대공약수 * 약수가 아닌 인수
    least_common_multiple *= greatest_common_denominator
    
    return [greatest_common_denominator, least_common_multiple]

def get_divisors(num): # 숫자 소인수분해
    divisors = [1]
    divisor = 2
    
    while (num >= divisor):
        if (num % divisor == 0):
            divisors.append(divisor)
            num /= divisor
        else:
            divisor += 1
            
    return divisors
        
        