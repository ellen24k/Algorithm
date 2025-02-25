def solution(players, m, k):
    answer = 0 # 서버 증설 횟수
    operating_servers_by_time = [0]*24 # 시간대별 운영 중인 서버 수
    needed_servers = [i//m for i in players] # 시간대별 필요한 서버의 수
    
    for i, needed_server in enumerate(needed_servers):
        if operating_servers_by_time[i] < needed_server:
            expansion = needed_server - operating_servers_by_time[i]
            answer += expansion
            
            for j in range(k):
                temp_idx = i + j
                if temp_idx < len(players):
                    operating_servers_by_time[temp_idx] += expansion
    return answer