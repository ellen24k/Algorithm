def solution(arr1, arr2):
    answer = list()
    
    for i in range(0,len(arr1)):
        temp = []
        
        for j in range(0,len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])
            
        answer.append(temp)
    
    return answer