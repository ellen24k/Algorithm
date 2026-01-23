def solution(my_string):
    ops = my_string.split()
    op_stack = []
    answer = 0
    
    for op in ops:
        if (op.isnumeric()):
            if (op_stack and (op_stack.pop() == '-')): answer -= int(op)
            else: answer += int(op)
        else: op_stack.append(op) 
    return answer