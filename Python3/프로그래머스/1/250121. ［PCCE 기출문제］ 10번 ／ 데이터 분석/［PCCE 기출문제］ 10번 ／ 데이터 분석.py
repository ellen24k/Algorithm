def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    criteria_dict = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    valid_list = [d for d in data if d[criteria_dict[ext]] < val_ext]
    return sorted(valid_list, key=lambda x: x[criteria_dict[sort_by]])