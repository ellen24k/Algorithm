def solution(brown, yellow):    
    brown = (brown-4)//2

    for i in range(1,brown):
         if i*(brown-i) == yellow:
                return [brown-i+2,i+2]
    