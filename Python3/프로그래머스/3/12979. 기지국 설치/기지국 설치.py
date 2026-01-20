def solution(n, stations, w):
    answer = 0
    uncovered = 1
    station_idx = -len(stations)
    stations_covering_from = [range(station-w, station+w+1) for station in stations]
    
    while (uncovered <= n):
        if (station_idx < -1 and stations[station_idx] + w < uncovered): station_idx += 1
        if (uncovered in stations_covering_from[station_idx]): 
            uncovered = stations[station_idx] + w + 1
        else:
            answer += 1
            uncovered += 2 * w + 1
        # print(answer, uncovered, stations_covering_from[station_idx])

    return answer