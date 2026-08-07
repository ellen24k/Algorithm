def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk or stk[-1] != arr[i]:
            stk.append(arr[i])
        else:
            stk.pop()
        i += 1
    return stk if stk else [-1]