from collections import deque

def solution(s):
    n = len(s)
    if n % 2 != 0: return 0

    deq = deque(s)
    pair = {')': '(', '}': '{', ']': '['}
    answer = 0
    rotate_sum = 0

    while rotate_sum < n:
        stack = []
        broken_idx = -1

        for i, ch in enumerate(deq):
            if ch in '([{': stack.append(ch)
            else:
                if not stack or stack[-1] != pair[ch]:
                    broken_idx = i
                    break
                stack.pop()

        if broken_idx == -1 and not stack:
            answer += 1
            deq.rotate(-1)
            rotate_sum += 1
            continue

        step = broken_idx + 1
        deq.rotate(-step)
        rotate_sum += step

    return answer
