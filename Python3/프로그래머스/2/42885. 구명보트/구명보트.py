def solution(people, limit):
    answer = 0
    first = 0
    last = len(people) - 1
    people.sort()
    
    for i in range(len(people)):    
        if (people[first] + people[last] <= limit):
            first += 1
            
        last -= 1
        answer += 1    
        
        if(first > last): break
    
    return answer