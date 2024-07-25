def dfs(name, visited, count, index, total, back, weight):
    visited[index] = True
    # print(name, visited, count, index, total, back, weight)
    if count < total:
        if False in visited:
            if not back:
                if name[index + weight] == "A":
                    total = dfs(name, visited, count + 1, index - weight, total, True, -weight)
                total = dfs(name, visited, count + 1, index + weight, total, False, weight)
            else:
                total = dfs(name, visited, count + 1, index + weight, total, True, weight)
        else:
            total = count

    # print("v",visited,"t:",total)
    if name[index] != "A": visited[index] = False
    return total

def make_alpha(char): # 커서 이동 제외 알파벳 완성을 위한 조작 횟수
    move_count = 0

    if char != "A":
        if char > "N":
            move_count = ord('Z') - ord(char) + 1
        else:
            move_count = ord(char) - ord('A')
    # A: 65 / N: 78 / Z: 90
    return move_count

def solution(name):
    answer = []
    for char in name:
        answer.append(make_alpha(char))
    # print(answer, "sum:", sum(answer))

    total = len(name) - 1

    if "A" in name:
        # print("t ori:", total)
        moved = [False if answer[i] else True for i in range(len(name))]
        # print("moved 초기:",moved)
        total = dfs(name, moved, 0, 0, total, False, 1)
        # print("t 1:", total)
        total = dfs(name, moved, 0, 0, total, False, -1)
        # print("t -1:",total)

    return sum(answer) + total