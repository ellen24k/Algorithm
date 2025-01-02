#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string my_string, vector<int> indices) {
    string answer = "";
    sort(indices.begin(), indices.end());
    
    for (int i = 0, indice_idx = 0; i < my_string.length(); i++){
        if (i != indices[indice_idx]) answer += my_string[i];
        else if (indice_idx < indices.size()) indice_idx++;
    }
    return answer;
}