#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<int> emergency) {
    map<int, int> emergency_map;
    vector<int> answer(emergency);
    for (int i: emergency) emergency_map[-i]; //map은 기본적으로 key 기준 오름차순 정렬
    
    int order = 1;
    for (auto& e : emergency_map) { e.second = order++; }
    for (auto& elem: answer)
        elem = emergency_map[-elem];
    return answer;
}