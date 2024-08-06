def solution(bandage, health, attacks):
    attack_dict = {attack[0]: attack[1] for attack in attacks}
    max_health = health
    count = 0
    # print("attack dict:", attack_dict)
    for t in range(1, attacks[-1][0] + 1):
        if t not in attack_dict:
            count += 1
            health = min(max_health, health + bandage[1] if count < bandage[0] else health + bandage[1] + bandage[2])
            if count >= bandage[0]: count = 0
        else: 
            health -= attack_dict[t]
            count = 0
        # print(t, health, count)
        
        if health <= 0: return -1
    return health