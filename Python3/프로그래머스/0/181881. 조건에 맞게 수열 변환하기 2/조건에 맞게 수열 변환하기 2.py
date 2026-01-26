def solution(arr):
    answer = 0
    
    def transform(a):
        res = []
        for num in a:
            if num >= 50 and num % 2 == 0:
                res.append(num // 2)
            elif num < 50 and num % 2 == 1:
                res.append(num * 2 + 1)
            else:
                res.append(num)
        return res
    
    while True:
        next_arr = transform(arr)
        if next_arr == arr:
            return answer
        answer += 1
        arr = next_arr
