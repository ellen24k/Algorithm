def solution(picture, k):
    answer = []
    for line in picture:
        newLine = ""
        
        for char in line:
            newLine += char * k
        
        for i in range(k):
            answer.append(newLine)
    return answer