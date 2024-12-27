from collections import defaultdict
def solution(routes):
    routes.sort(key= lambda route: route[1])
    cctv_s = []
    cnt = 0
    
    for route in routes:
        already_coverable = False
    
        for cctv in cctv_s[::-1]:
            if route[0] <= cctv <= route[1]: 
                already_coverable = True
                break
        
        if not already_coverable:
            cctv_s.append(route[1])
            cnt += 1
            
    # print(routes)
    return cnt
    
    