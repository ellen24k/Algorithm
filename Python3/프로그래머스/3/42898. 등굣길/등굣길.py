def solution(m, n, puddles):
    coordinate = [[1 for _ in range(m)] for _ in range(n)]
    coordinate[-1][-1] = -1

    for puddle in puddles:
        # print("pud:",puddle)
        if puddle[0] == 1:  
            for i in range(puddle[1] - 1, n):
                coordinate[i][0] = 0
        elif puddle[1] == 1:
            for i in range(puddle[0] - 1, m):
                coordinate[0][i] = 0
        else:
            coordinate[puddle[1] - 1][puddle[0] - 1] = 0

    # for row in coordinate:
    #     print(row)

    for row in range(1, n):
        for col in range(1, m):
            if coordinate[row][col] != 0:
                coordinate[row][col] = (coordinate[row - 1][col] + coordinate[row][col - 1]) % 1000000007

    # print()
    # for row in coordinate:
    #     print(row)

    return coordinate[-1][-1] if coordinate[-1][-1] != -1 else 0