from datetime import timedelta

def solution(video_len, pos, op_start, op_end, commands):
    video_time = timedelta(minutes=int(video_len[:2]), seconds=int(video_len[3:]))
    op_start_time = timedelta(minutes=int(op_start[:2]), seconds=int(op_start[3:]))
    op_end_time = timedelta(minutes=int(op_end[:2]), seconds=int(op_end[3:]))
    move_interval = timedelta(seconds=10)
    answer = timedelta(minutes=int(pos[:2]), seconds=int(pos[3:]))
    
    for command in commands:
        if op_start_time <= answer <= op_end_time: answer = op_end_time
        
        if command == 'next': 
            answer += move_interval
            if answer > video_time: answer = video_time
        else: 
            answer -= move_interval
            if answer < timedelta(): answer = timedelta()
            
        if op_start_time <= answer <= op_end_time: answer = op_end_time
    return str(answer)[2:]