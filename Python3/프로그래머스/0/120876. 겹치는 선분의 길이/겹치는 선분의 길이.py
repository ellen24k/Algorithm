from collections import defaultdict

def solution(lines):
    dots = defaultdict(int)

    for start, end in lines:
        for x in range(start, end):
            dots[x] += 1

    answer = 0
    x = min(dots.keys())
    max_x = max(dots.keys())

    while x <= max_x:
        if dots[x] >= 2:
            start = x
            while x <= max_x and dots[x] >= 2: 
                x += 1
            answer += x - start
        else: x += 1

    return answer
