#include <unordered_set>
#include <string>

using namespace std;

string solution(string my_string) {
    unordered_set<char> seen;
    string answer;
    answer.reserve(my_string.size());  // 미리 충분한 공간 할당

    for (char c : my_string) 
        if (seen.insert(c).second) answer += c;

    answer.shrink_to_fit();  // 사용하지 않는 공간 해제
    return answer;
}
