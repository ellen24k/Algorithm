def solution(str_list):
    for i, chr in enumerate(str_list):
        if chr == 'l': return str_list[:i]
        if chr == 'r': return str_list[i + 1:]
    return []