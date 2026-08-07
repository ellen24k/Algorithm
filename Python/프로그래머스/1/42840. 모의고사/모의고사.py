def solution(answers):
    answer = []
    
    supoja_1 = [1,2,3,4,5]
    supoja_2 = [2,1,2,3,2,4,2,5]
    supoja_3 = [3,3,1,1,2,2,4,4,5,5]
    cor_count = [0,0,0]
    
    for i,v in enumerate(answers):
        if supoja_1[i%5] == v: #len(supoja_1) = 5
            cor_count[0] += 1
        if supoja_2[i%8] == v: #len(supoja_2) = 8
            cor_count[1] += 1
        if supoja_3[i%10] == v: #len(supoja_3) = 10
            cor_count[2] += 1
        
    # print(cor_count)
    for i,v in enumerate(cor_count):
        if v == max(cor_count):
            answer.append(i + 1)
    
    return answer