def solution(n, lost, reserve):
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))
    # print("l:", lost, "r:", reserve)
    answer = n - len(lost)

    for l in lost:
        for r in reserve:
            # print("l:", l, "r:", r)
            if l == r - 1 or l == r + 1:
                reserve.remove(r)
                # print("r:",r,"->","l:",l)
                answer += 1
                break
                
        # print("l:", lost, "r:", reserve)

    return answer