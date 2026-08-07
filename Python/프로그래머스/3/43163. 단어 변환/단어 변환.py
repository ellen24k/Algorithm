from collections import deque

def bfs(begin, target, words, used):
    # [시작 단어, visited에서 시작 단어의 인덱스] -> ['hit', 0]
    queue = deque([[begin,-1]]) 

    while(queue):
        [word, index] = queue.popleft()
        # print([word,index])
        for i in range(len(words)): # ["hot", "dot", "dog", "lot", "log", "cog"]
            if (used[i] == 0): # 사용한 적 없는 단어인지 확인
                dif_count = 0
                # print("dif check:",word,words[i])
                for j in range(len(word)): # 다른 글자 개수 확인
                    if word[j] != words[i][j]:
                        dif_count += 1
                # print("dif:",dif_count)
                if dif_count == 1: # 한 글자만 달라야 변환 가능
                    queue.append([words[i],i])
                    used[i] = used[index] + 1
                    # print(queue, used)
    return used[words.index(target)]


def solution(begin, target, words):
    if target not in words: return 0 # 변환 불가능

    used = [0 for _ in range(len(words))] # [0, 0, 0, 0, 0, 0, 0]

    return bfs(begin, target, words, used)
