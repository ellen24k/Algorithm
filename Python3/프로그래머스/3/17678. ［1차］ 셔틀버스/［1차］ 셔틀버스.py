def time_to_min(time_str):
    return int(time_str[:2])*60 + int(time_str[3:])

def min_to_time(minutes):
    return f'{minutes//60:02}:{minutes%60:02}'

def solution(n, t, m, timetable):
    # 크루들의 도착 시간을 분 단위로 변환해 내림차순 정렬
    minute_timetable = sorted([time_to_min(t) for t in timetable], reverse=True)    
    shuttle_departure_time = 540 # 09:00
    no_waiting_line = False
    
    # 마지막 셔틀이 오기 전까지 콘은 사무실로 가지 않는다
    for shuttle_operation_cnt in range(n - 1):
        # print(f'cur dep time: {min_to_time(shuttle_departure_time)}')
        for shuttle_capacity in range(m):
            if minute_timetable:
                if minute_timetable[-1] <= shuttle_departure_time:
                    minute_timetable.pop()
                else: continue
            else:
                no_waiting_line = True
                break
                
        if no_waiting_line: break
            
        shuttle_departure_time += t
    
    # print('final dep time: ' + min_to_time(shuttle_departure_time))
    # 대기열의 길이가 셔틀의 최대 수용 인원 이상이라면, 콘은 대기열의 m번째에 서 있으면 된다
    if minute_timetable and len(minute_timetable) >= m:
        if minute_timetable[-m] <= shuttle_departure_time:
            return min_to_time(minute_timetable[-m] - 1)

    # 대기열이 최대 수용 인원보다 짧다면, 셔틀 출발 시간에 맞춰 도착하면 된다
    return min_to_time(shuttle_departure_time)