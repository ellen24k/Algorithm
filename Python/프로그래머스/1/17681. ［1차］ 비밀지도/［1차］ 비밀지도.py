def solution(n, arr1, arr2):
    answer = list()
    converted_arr = compare_binary(n,arr1,arr2)
    
    for i in converted_arr:
        answer.append(''.join(map(lambda x: '#' if x=='1' else ' ',i)))
    
    return answer

def compare_binary(n,arr1,arr2):
    compared_arr = list()
    
    for index in range(n):
        binary = bin(arr1[index]|arr2[index]) # 비트 OR
        compared_arr.append(binary[2:].zfill(n)) 
        # [2:] : 'ob' 접두사 제외한 형태 반환
        # zfill : 지정한 길이만큼 문자열 0으로 채우기, 기존 문자열 길이 포함해서 계산

    return compared_arr
    