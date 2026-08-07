def solution(mats, park):
    park_r = len(park)
    park_c = len(park[0])

    # 큰 사이즈 매트 부터 비교
    mats.sort(reverse=True)
    for mat in mats:
        # 전체 매트를 깔 수 있는 자리에 대해 비교
        for start_r in range(park_r - mat + 1):
            for start_c in range(park_c - mat + 1):
                # 매트 영역 내 사용중인 자리 확인
                for i in range(start_r, start_r + mat):
                    if {"-1"} != set(park[i][start_c:start_c + mat]):
                        break
                # 빈 자리인 경우 해당 매트 깔 수 있음
                else:
                    return mat
                    
    return -1