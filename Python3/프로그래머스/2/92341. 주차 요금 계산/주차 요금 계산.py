from collections import defaultdict
from datetime import datetime

def make_dict_by_car(records):
    def dict_value():
        return [[], []] # [[in], [out]]
    parking_records_by_car = defaultdict(dict_value)    

    for record in records:
        record = record.split() # ' ' 기준 split
        # print(record)
        if record[2] == 'IN':
            parking_records_by_car[record[1]][0].append(record[0])
        else: parking_records_by_car[record[1]][1].append(record[0])
    # print(parking_records_by_car)
    return parking_records_by_car

def calculate_fees(fees, car_record):
    total_parking_time = 0 # 총 주차시간
    # print(car_record)
    
    for i in range(len(car_record[1])):
        in_time = datetime.strptime(car_record[0][i], '%H:%M')
        out_time = datetime.strptime(car_record[1][i], '%H:%M')
        total_parking_time += (out_time - in_time).seconds // 60 # 시간 차이를 분 단위로 계산
        
    if len(car_record[0]) > len(car_record[1]): # 마지막 out 기록이 없는 경우
        total_parking_time += (datetime(1900,1,1,23,59) - datetime.strptime(car_record[0][-1], '%H:%M')).seconds // 60
    # print(total_parking_time)
    
    total_fee = fees[1]
    if total_parking_time > fees[0]:
        total_parking_time -= fees[0]
        total_parking_time = (total_parking_time + fees[2] - 1) // fees[2]
        
        total_fee += total_parking_time * fees[3]
    return total_fee
    

def solution(fees, records):
    answer = []
    records.sort(key = lambda x: x[6:10])
    parking_records_by_car = make_dict_by_car(records)
    
    for parking_record in parking_records_by_car.values(): # values
        answer.append(calculate_fees(fees, parking_record))
        # answer.append() 
    return answer