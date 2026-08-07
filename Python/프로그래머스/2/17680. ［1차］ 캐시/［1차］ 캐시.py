from collections import OrderedDict

def solution(cacheSize, cities):
    answer = 0
    cached = OrderedDict()
    for city in cities:
        city = city.lower()
        if (city in cached):
            cached.move_to_end(city)
            answer += 1
        else:
            cached.update({city: None})
            answer += 5
            if (len(cached) > cacheSize): cached.popitem(last=False)
        # print(city, cached, answer)
    return answer