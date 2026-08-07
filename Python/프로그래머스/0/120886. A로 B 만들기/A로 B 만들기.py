def solution(before, after):
    return (sorted(list(before)) == sorted(list(after))) * 1

# def solution(before, after):
#     bef_set = set(before)
#     aft_set = set(after)
#     for before_chr in bef_set:
#         if before.count(before_chr) != after.count(before_chr): return 0
#     return 1