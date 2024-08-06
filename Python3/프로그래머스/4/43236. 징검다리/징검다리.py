def solution(distance, rocks, n):
    if n == len(rocks): return distance

    left = 0; right = distance; mid = 0
    rocks += [0,distance]
    rocks.sort()
    
    rock_distance = [rocks[i] - rocks[i-1] for i in range(1,len(rocks))]
    # print('d:', rock_distance)
    while(left <= right):
        mid = (left + right) // 2
        count = 0
        distance = 0
        for i in rock_distance:
            distance += i
            # print('cnt:', count,'mid:', mid,'distance', distance, i)
            if distance < mid:
                count += 1
                if count > n: break
            else: 
                distance = 0
        if count > n: right = mid - 1
        else: left = mid + 1
        # print("--- left:",left, "right:",right)
    return right

# print(solution(25, [2, 14, 11, 21, 17], 2))  # Expected output: 4
# print(solution(16, [4, 8, 11], 2))           # Expected output: 8
# print(solution(10, [3, 5, 7], 1))            # Expected output: 3