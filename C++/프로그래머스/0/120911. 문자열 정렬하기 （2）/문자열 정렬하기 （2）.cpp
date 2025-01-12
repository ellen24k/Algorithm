#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string my_string) {
    string answer = "";
    for (char c : my_string) answer += (c < 'a') ? c + 'a' - 'A' : c;
    sort(answer.begin(), answer.end());
    return answer;
}