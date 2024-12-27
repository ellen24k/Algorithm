#include <string>
#include <vector>

using namespace std;

vector<int> solution(string myString) {
    vector<int> answer;
    int between_x_cnt = 0;
    
    for (int i = 0; i < myString.length(); i++){
        if (myString[i] != 'x') between_x_cnt++;
        else {
            answer.push_back(between_x_cnt);
            between_x_cnt = 0;
        }
    }
    answer.push_back(between_x_cnt);
    
    return answer;
}