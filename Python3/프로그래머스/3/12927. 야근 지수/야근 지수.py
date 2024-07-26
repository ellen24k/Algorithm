def solution(n, works):
    answer = 0
    works.sort(reverse = True)
    print(works)

    index = 0
    while(n > 0):
        if works[0] == 0: return 0
        while(works[index] == works[index+1]):
            index += 1
            if index == len(works) -1: break
        # print(n, index)

        works[index] -= 1
        n -= 1
        if index != 0: index -= 1

    for work in works:
        answer += work * work
        # print(work,end="")
    # print()
    return answer