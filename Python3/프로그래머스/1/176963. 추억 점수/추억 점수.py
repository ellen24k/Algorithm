def solution(name, yearning, photo):
    answer = [0 for i in range(len(photo))]
    
    # enumerate 함수로 인덱스(key)와 값(value)를 추출 가능
    for index,i in enumerate(photo):
        # print(i)
        for j in i:
            if j in name: answer[index] += yearning[name.index(j)]
            
        index += 1;
    
    return answer