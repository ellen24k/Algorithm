def solution(new_id):
    answer = ''
    # step 1
    step_1 = []
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in new_id:
        if c in upper: # 리스트 컴프리헨션
            step_1.append(lower[upper.index(c)])
        else:
            step_1.append(c)
    # print(step_1)
    
    # step_2
    restriction_2 = 'abcdefghijklmnopqrstuvwxyz0123456789-_.' # 정규식
    step_2 = [c for c in step_1 if c in restriction_2]
    # print(step_2)
    
    # step_3
    # step_3 = ''.join(step_2)
    # step_3.replace('..', '.') # ... 등 처리 필요
    continuous_dot = False
    step_3 = []
    for idx, c in enumerate(step_2):
        if c == '.':
            # if idx != 0: 
            continuous_dot = True
        else:
            if continuous_dot:
                step_3.append('.')
                continuous_dot = False
            step_3.append(c)
    # if continuous_dot:
        # step_3.append('.') # 마지막에 .으로 끝난 경우?
    # print(step_3)
    
    # step_4
    if len(step_3) > 1:
        if step_3[0] == '.':
            step_3 = step_3[1:]
        if step_3[-1] == '.':
            step_3 = step_3[:len(step_3)-1]
    else:
        if step_3 and step_3[0] == '.':
            step_3 = []
            
    
#     if step_3[0] == '.':
#         if len(step_3) > 1:
#             step_3 = step_3[1:]
#         else:
#             step_3 = []
#     if step_3[-1] == '.':
#         step_3 = step_3[:len(step_3-1)]
    
    # step_5
    if not step_3: 
        step_3 = ['a']
        
    # step_6
    step_6 = step_3[:15]
    if step_6[-1] == '.':
        step_6 = step_6[:14]
    # print(len(step_6))

    # step_7
    while len(step_6) <= 2:
        step_6.append(step_6[-1])
    # print(step_6)
    
            
    
    return ''.join(step_6)