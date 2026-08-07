def solution(dots):
    width = max(abs(dots[0][0] - dots[1][0]),abs(dots[0][0] - dots[2][0]))
    height = max(abs(dots[0][1] - dots[1][1]),abs(dots[0][1] - dots[2][1]))
    return width * height