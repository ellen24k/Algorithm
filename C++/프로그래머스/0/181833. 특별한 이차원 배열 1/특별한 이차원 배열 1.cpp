#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(int n) {
    vector<vector<int>> answer;
    for (int i = 0; i < n; i++){
        vector<int> vector_row;
        for(int j = 0; j < n; j++) vector_row.push_back((j==i) ? 1 : 0);
        answer.push_back(vector_row);
    }
    
    return answer;
}