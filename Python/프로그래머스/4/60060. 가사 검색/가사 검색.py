# 4차 시도: Trie + 길이에 따라 words 구분, 성공, 정확도 18번 29.14ms / 효율성 3번 1590.51ms

from collections import defaultdict

class Node:
    __slots__ = ['children', 'count']

    def __init__(self):
        self.children = defaultdict(Node)
        self.count = 0 # 해당 글자까지 겹치는 단어 수

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        cur_node = self.head
        for i in range(len(word)):
            cur_node.count += 1
            cur_node = cur_node.children[word[i]]
        # cur_node.count += 1

    def search(self, query):
        cur_node = self.head

        for i in range(query.index('?')):
            if query[i] not in cur_node.children: return 0 # 겹치는 글자가 없음
            cur_node = cur_node.children[query[i]]

        return cur_node.count


def solution(words, queries):
    word_len_dict = {} # 가사의 길이에 따른 (정/역방향 trie)
    query_count = len(queries) # 쿼리의 수
    answer = [0 for _ in range(query_count)]

    for word in words:
        length_w = len(word)
        if length_w not in word_len_dict:
            word_len_dict[length_w] = (Trie(), Trie())  # (순방향, 역방향)

        word_len_dict[length_w][0].insert(word)
        word_len_dict[length_w][1].insert(word[::-1]) # 역방향 탐색을 위해 word를 뒤집어서 삽입

    for i in range(query_count):
        length_q = len(queries[i])
        if length_q in word_len_dict:
            if queries[i][0] == '?':
                answer[i] += word_len_dict[length_q][1].search(queries[i][::-1])
            else:
                answer[i] += word_len_dict[length_q][0].search(queries[i])
        # print(queries[i], answer[i])

    return answer


# 3차 시도:  Trie 사용, 성공, 정확도 18번 42.19ms / 효율성 3번 2567.71ms

# from collections import defaultdict

# class Node:
#     __slots__ = ['children', 'remaining_length']
    
#     def __init__(self):
#         self.children = defaultdict(Node)
#         self.remaining_length = defaultdict(int)

# class Trie:
#     def __init__(self):
#         self.head = Node()
    
#     def insert(self, str):
#         cur_node = self.head
#         length = len(str)
#         for i in range(length):
#             cur_node.remaining_length[length - i] += 1
#             cur_node = cur_node.children[str[i]]
#             # print(str, cur_node.children,cur_node.remaining_length)
#         # cur_node.remaining_length[0] += 1
    
#     def search(self, str):
#         cur_node = self.head
#         indexQ = str.index('?')
#         countQ = len(str) - indexQ
        
#         for i in range(indexQ):
#             if str[i] not in cur_node.children: return 0
#             cur_node = cur_node.children[str[i]]
            
#         return cur_node.remaining_length[countQ]
    
# def solution(words, queries):
#     lenQ = len(queries)
#     trie = Trie()
#     back_trie = Trie()
#     query_cache = {}
#     answer = [0 for _ in range(lenQ)]
    
#     for word in words:
#         trie.insert(word)
#         back_trie.insert(word[::-1])
    
    
#     for i in range(lenQ):
#         if queries[i] in query_cache:
#             answer[i] += query_cache[queries[i]]
#         else:
#             if queries[i][0] == '?':
#                 answer[i] += back_trie.search(queries[i][::-1])
#             else: 
#                 answer[i] += trie.search(queries[i])
#             query_cache[queries[i]] = answer[i]
            
#     # print(answer)
#     return answer

# 2차 시도: words의 길이를 기준으로 딕셔너리를 만들어 문자열의 길이가 같은 경우에만 비교, 효율성 시간초과 -> 정확도 18번 31.62ms

# def make_dict_by_len(list_sample):
#     dict = {}
#     for i in list_sample:
#         length = len(i)
#         if length in dict: dict[length].append(i)
#         else: dict[length] = [i]
#     return dict

# def solution(words, queries):
#     answer = [0 for _ in range(len(queries))]
#     words = make_dict_by_len(words)
    
#     for i,query in enumerate(queries):
#         length = len(query)
#         if length in words:
#             startQ = query[0] == '?' # ?로 시작하는가
#             countQ = query.count('?') if startQ else query.find('?')
#             for word in words[length]:
#                 if startQ:
#                     if word.endswith(query[countQ:]):
#                         answer[i] += 1
#                 else:
#                     if word.startswith(query[:countQ]):
#                         answer[i] += 1
#     return answer

# 1차 시도: 정규식 이용, 효율성 시간초과 -> 정확도 18번 613ms
# import re

# def solution(words, queries):
#     answer = []
#     query_list = [re.sub('\?','.',query) for query in queries]
    
#     for query in query_list:
#         answer.append(sum(1 for word in words if re.fullmatch(query,word)))
#     return answer

# match : word가 query로 시작하는가
# fullmatch : word가 query와 일치하는가

