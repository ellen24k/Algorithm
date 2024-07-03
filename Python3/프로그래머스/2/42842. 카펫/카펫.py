def solution(brown, yellow):    
    brown = (brown-4)//2 # 가로 + 세로의 길이

    for i in range(1,brown):
         if i*(brown-i) == yellow:
                return [brown-i+2,i+2]
    