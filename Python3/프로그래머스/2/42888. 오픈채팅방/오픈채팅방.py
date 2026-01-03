def solution(record):
    nicknames = dict()
    uidRec = []
    actRec = []
    
    for rec in record:
        parts = rec.split() # parts[0] = act, parts[1] = uid, parts[2] = nickname
        if parts[0] == 'Leave':
            uidRec.append(parts[1])
            actRec.append('님이 나갔습니다.')
        else:
            nicknames[parts[1]] = parts[2]
            if parts[0] == 'Enter':
                uidRec.append(parts[1])
                actRec.append('님이 들어왔습니다.')
        
    answer = [f'{nicknames[uidRec[i]]}'+ parts[0] for i, parts[0] in enumerate(actRec)]
    
    return answer