def solution(dots):
    def slope(p1, p2):
        return (p1[1] - p2[1], p1[0] - p2[0])  # (dy, dx)

    cases = [
        (0, 1, 2, 3),
        (0, 2, 1, 3),
        (0, 3, 1, 2)
    ]

    for a, b, c, d in cases:
        dy1, dx1 = slope(dots[a], dots[b])
        dy2, dx2 = slope(dots[c], dots[d])
        if dy1 * dx2 == dy2 * dx1:
            return 1

    return 0