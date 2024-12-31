#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(vector<string> s1, vector<string> s2) {
    set<string> s_set;
    s1.insert(s1.end(), s2.begin(), s2.end());
    for (string elem: s1) s_set.insert(elem);
    
    return s1.size() - s_set.size();
}