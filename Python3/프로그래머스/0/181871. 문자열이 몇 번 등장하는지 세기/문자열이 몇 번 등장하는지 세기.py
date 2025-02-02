def solution(myString, pat):
    count = 0
    start = 0
    
    while start <= len(myString) - len(pat):
        pos = myString.find(pat, start)
        if pos != -1:
            count += 1
            start = pos + 1
        else:
            break
    
    return count
