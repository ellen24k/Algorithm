def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = {x: dice.count(x) for x in dice}
    
    items = list(counts.items())

    if len(items) == 1:
        p = items[0][0]
        return 1111 * p

    if len(items) == 2:
        (n1, c1), (n2, c2) = items
        if c1 == 3: return (10 * n1 + n2) ** 2
        if c2 == 3: return (10 * n2 + n1) ** 2
        return (n1 + n2) * abs(n1 - n2)

    if len(items) == 3:
        for n, c in items:
            if c == 2:
                others = [x for x, cnt in items if cnt == 1]
                return others[0] * others[1]

    return min(dice)
