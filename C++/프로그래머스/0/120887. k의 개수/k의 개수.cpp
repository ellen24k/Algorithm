#include <string>
#include <vector>

using namespace std;

int solution(int i, int j, int k) {
    int answer = 0;
    char k_chr = '0' + k;
    for (int start = i, end = j; start <= end; start++) {
        string temp = to_string(start);
        for (char cur : temp) if (cur == k_chr) answer++;
    }
    return answer;
}