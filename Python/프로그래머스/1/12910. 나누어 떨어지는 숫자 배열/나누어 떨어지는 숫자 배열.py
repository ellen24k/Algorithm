def solution(arr, divisor):
    answer = sorted([element for element in arr if element%divisor==0])
    
    if(len(answer) == 0):
        return [-1]
    else:
        return answer