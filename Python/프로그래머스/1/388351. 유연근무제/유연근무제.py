def solution(schedules, timelogs, startday):
    answer = 0
    
    for i, schedule in enumerate(schedules):
        cur_day = startday - 1
        schedule += 10
        late = False
        
        if schedule % 100 >= 60:
            schedule += 100 - schedule % 100 + schedule % 10
        
        for timelog in timelogs[i]:
            if cur_day not in (5,6): # 평일이면
                if timelog > schedule: 
                    late = True
                    break
            cur_day = (cur_day + 1)%7
            
        if not late: answer += 1
    return answer