def solution(numbers):
    answer = [-1] * len(numbers)
    numStack = []
    for i, num in enumerate(numbers):
        while (numStack and numbers[numStack[-1]] < num):
            answer[numStack.pop()] = num        
        numStack.append(i)
        
    return answer