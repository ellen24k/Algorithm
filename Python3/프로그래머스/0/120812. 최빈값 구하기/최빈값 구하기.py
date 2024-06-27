def solution(array):
    array.sort()
    
    answer = array[0]
    answer_count = array.count(array[0])
    not_only = False
    
    for i in range(0,len(array)-1):
        if array[i] != array[i+1]:
            if answer_count < array.count(array[i+1]):
                
                answer_count = array.count(array[i+1])
                answer = array[i+1]
                not_only = False
                
            elif answer_count == array.count(array[i+1]):
                not_only = True
                
    if not_only:
        return -1
    else:
        return answer