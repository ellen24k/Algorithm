import re

def solution(new_id):
    answer = new_id.lower() # step 1
    answer = re.sub('[^\w\-.]', '', answer) # step 2
    answer = re.sub('[.]+', '.', answer) # step 3
    answer = re.sub('^[.]|[.]$', '', answer) # step 4
    if answer == '': answer = 'a' # step 5
    # step 6
    if len(answer) >= 16: answer = answer[:15] if answer[14] != '.' else answer[:14]
    # step 7
    answer = answer if len(answer) > 2 else answer + ''.join([answer[-1] for _ in range(3-len(answer))])
        
    # print(answer)
    return answer

# re.sub(pattern, replace, text) >> text 중 pattern에 해당하는 부분을 replace로 치환.
# \w >> 'alphanumeric' + '_'