from collections import deque

def solution(numbers, direction):
    q = deque(numbers)
    q.rotate() if direction == 'right' else q.rotate(-1)
    return list(q)