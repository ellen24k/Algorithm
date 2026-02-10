from itertools import combinations

def solution(n, q, ans):
    answer = 0
    not_ans = []
    
    # 0 조합 수 제외 후 리스트 생성
    if 0 in ans: 
        for i, a in enumerate(ans): 
            if not a : 
                not_ans += q[i]
    set_q = [set(i) for i in q]
    nums = list(i for i in range(1, n + 1) if i not in not_ans)
    comb = combinations(nums, 5)
    
    for c in comb:
        available_comb = True
        
        for i, q_elem in enumerate(set_q):
            if len(set(c) & q_elem) != ans[i]:
                available_comb = False
                break
                
        if available_comb: answer += 1
            
    return answer