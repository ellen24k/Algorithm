def solution(genres, plays):
    answer = []
    genre_dict = {} # {genre, [(song_index, song_play)]}
    
    for index in range(len(genres)): # 장르에 따라 곡 분류
        if genres[index] in genre_dict:
            genre_dict[genres[index]].append((index, plays[index]))
        else:
            genre_dict[genres[index]] = [(index, plays[index])]
        
    # print("g:", genre_dict)
    genre_values = sorted(genre_dict.values(), key= lambda value_list: -sum((x[1] for x in value_list))) # 장르 별 총 재생 횟수 기준 내림차순
    # print("v:", genre_values)
    for value in genre_values:
        value.sort(key=lambda x: (-x[1], x[0])) # 재생 횟수 내림차순, 곡명 오름차순
        for i in range(2):
            if i <= len(value) - 1:
                answer.append(value[i][0])
            
    # print("a:",answer)
    return answer