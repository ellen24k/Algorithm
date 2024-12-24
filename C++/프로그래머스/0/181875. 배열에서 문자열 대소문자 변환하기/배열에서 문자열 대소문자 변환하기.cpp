#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> strArr) {
    vector<string> answer;
    for (size_t i = 0; i < strArr.size(); ++i) {
        string transformed;
        for (char c : strArr[i]) {
            if (i % 2 == 0) {
                transformed += tolower(c);
            } else {
                transformed += toupper(c);
            }
        }
        answer.push_back(transformed);
    }
    return answer;
}