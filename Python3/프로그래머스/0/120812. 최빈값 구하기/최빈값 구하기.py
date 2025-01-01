from collections import defaultdict

def solution(array):
    freq = defaultdict(int)
    for elem in array: freq[elem] += 1
    
    sorted_arr = sorted(set(array), key= lambda elem: -freq[elem])
    # print(sorted_arr)
    
    if len(sorted_arr) > 1:
        return sorted_arr[0] if freq[sorted_arr[0]] > freq[sorted_arr[1]] else -1
    return sorted_arr[0]

    
# def solution(array):
#     array.sort()
    
#     answer = array[0]
#     answer_count = array.count(array[0])
#     not_only = False
    
#     for i in range(0,len(array)-1):
#         if array[i] != array[i+1]:
#             if answer_count < array.count(array[i+1]):
                
#                 answer_count = array.count(array[i+1])
#                 answer = array[i+1]
#                 not_only = False
                
#             elif answer_count == array.count(array[i+1]):
#                 not_only = True
                
#     if not_only:
#         return -1
#     else:
#         return answer