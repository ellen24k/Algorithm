import math
from collections import defaultdict

# 노란불이 들어오는 주기 = n*(초+노+빨) + 처음 초록불 주기 + 1(초) 마다
def solution(signals):
    signal_dict = {}
    yellows = defaultdict(int)
    
    # 신호등 노란불 패턴은 각 신호등 반복 주기 공배수 단위로 반복?
    max = 1
    
    # 각 신호등의 노란불 주기 구하기
    for idx, signal in enumerate(signals):
        period = sum(signal)
        signal_dict[idx] = (signal[0] + 1, period, signal[1]) # 처음 노란불, 노란불 주기, 노란불 유지 시간
        max *= period
        
    # 노란불이 들어오는 초 계산
    for signal in signal_dict.items():
        # print(signal)
        # 노란불 최대 공배수 범위
        for i in range(max):
            # 유지 시간
            for j in range(signal[1][2]):
                # print(signal, i*signal[1][1] + j + signal[1][0])
                yellows[i*signal[1][1] + j + signal[1][0]] += 1
    # print(yellows)
    
    for y, cnt in yellows.items():
        if cnt == len(signals): return y
    return -1