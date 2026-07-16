# 각 층에 w개씩 택배를 쌓았을 때 택배 번호 max = w배수
# num번 상자의 층 수 == (num - 1) // w, 0층이 최하단
# 상자 쌓는 방향: 짝수 층에서 좌->우 홀수 층에서 우->좌
# 층 내에서의 offset으로 최상층에 박스가 있는지 확인
def solution(n, w, num):
    num_floor = (num - 1) // w
    total_floor = (n - 1) // w
    # if num_floor == total_floor: return 1
    # if num_floor % 2 == 0:
    num_floor_offset = num - w * num_floor # 1~w 범위
    total_floor_offset = n - w * total_floor # 1~w 범위
    # else:
        # num_floor_offset = num - w * num_floor
        
    # print(f'num of floor: {num_floor} | num off: {num_floor_offset}')
    # print(f'total of floor: {total_floor} | total off: {total_floor_offset}')
    
    # num층과 최상층 택배 쌓는 방향이 다르면(홀짝) offset(층 내에서) 합이 w+1 미만이면 택배 하나 덜 꺼내도 됨
    # 택배 쌓는 방향이 같으면 total offset이 num offset보다 작아야 덜 꺼낼 수 있음
    up_there = total_floor - num_floor
    if num_floor % 2 == total_floor % 2: # 방향 동일
        if num_floor_offset <= total_floor_offset:
            up_there += 1
    else:
        if num_floor_offset + total_floor_offset > w:
            # print(num_floor_offset + total_floor_offset)
            up_there += 1
    
    
    return up_there