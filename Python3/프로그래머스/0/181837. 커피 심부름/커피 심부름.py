def solution(order):
    answer = 0
    price = {'cafelatte': 5000, 'americano': 4500}
    for each_order in order:
        if each_order in ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]:
            answer += price['cafelatte']
        else:
            answer += price['americano']
    return answer