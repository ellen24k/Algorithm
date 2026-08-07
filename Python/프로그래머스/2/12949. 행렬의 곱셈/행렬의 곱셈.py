import numpy as np

def solution(arr1, arr2):
    array1 = np.array(arr1)
    array2 = np.array(arr2)
    
    answer = array1.dot(array2)
    
    return answer.tolist()