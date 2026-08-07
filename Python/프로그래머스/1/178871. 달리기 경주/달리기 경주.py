def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}

    for call in callings:
        i = rank[call]
        prev_player = players[i - 1]  

        players[i - 1], players[i] = players[i], players[i - 1]

        rank[call] -= 1
        rank[prev_player] += 1

    return players
