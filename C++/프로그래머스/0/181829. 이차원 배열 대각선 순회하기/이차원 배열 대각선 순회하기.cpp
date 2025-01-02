#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, int k) {
    int answer = 0;
    int i_max = board.size(), j_max = board[0].size();
    // cout << i_max << " " << j_max << endl;
    for(int i= 0; i < i_max; i++)
        for (int j = 0; j < j_max; j++){
            if (i + j <= k) answer += board[i][j];
            else break;
        }
    
    return answer;
}