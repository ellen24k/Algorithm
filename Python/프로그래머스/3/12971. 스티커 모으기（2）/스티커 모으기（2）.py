def solution(sticker):
    # can only choose 1 element
    if len(sticker) <= 3: return max(sticker)
    
    # dp0 can start with sticker[0]
    dp0 = sticker[:-1]
    dp0[2] += dp0[0]
    for idx in range(3, len(dp0)):
        dp0[idx] += max(dp0[idx-3:idx-1])
    
    # dp1 can start with sticker[1]
    dp1 = sticker[1:]
    dp1[2] += dp1[0]
    for idx in range(3, len(dp1)):
        dp1[idx] += max(dp1[idx-3:idx-1])
    
    return max(dp0[-1], dp0[-2], dp1[-1], dp1[-2])