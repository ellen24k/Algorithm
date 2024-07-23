def dfs(game_results, player, trace_code, trace_index):
    # print("player:", player + 1, "current game result:", game_results[player])

    for new_player in range(len(game_results)):
        # print(player+1,new_player+1)
        # 추적 코드에 맞는 플레이어의 대진 결과 반영
        if game_results[player][new_player] == trace_code and new_player not in trace_index:
            trace_index.append(new_player)
            dfs(game_results, new_player, trace_code, trace_index)
            # print(player + 1, "trace 결과:", trace_index)


def solution(n, results):
    game_results = [[0 for _ in range(n)] for _ in range(n)]
    # for player_num in range(1,n+1): # 경기결과 초기화
        # print(player_num,":",game_results[player_num-1])

    for result in results:  # results만을 가지고 경기결과 입력
        game_results[result[0] - 1][result[1] - 1] = 1  # 1 > 승리
        game_results[result[1] - 1][result[0] - 1] = -1  # -1 > 패배

    # for player_num in range(n): # 경기결과
        # print(player_num+1,":",game_results[player_num])

    for player in range(n):
        trace_up = []
        trace_down = []
        
        if game_results[player].count(0) > 1:
            # print("player:", player + 1, "winning game")
            dfs(game_results, player, 1,trace_up)
            # print(trace_up)
            for index in trace_up:
                game_results[player][index] = 1

            # print("player:", player + 1, "losing game")
            dfs(game_results, player, -1, trace_down)
            for index in trace_down:
                game_results[player][index] = -1

            # for player_num in range(n): # 경기결과
                # print(player_num+1,":",game_results[player_num])

    answer = 0
    for player_num in range(n):
        if game_results[player_num].count(0) == 1:
            answer += 1

    return answer