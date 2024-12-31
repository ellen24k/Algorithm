#include <string>
#include <vector>

using namespace std;

int solution(int order) {
    int answer = 0;
    while (order){
        int is_clap_num = order % 10;
        order /= 10;
        if (is_clap_num == 3 or is_clap_num == 6 or is_clap_num == 9) answer++;
    }
    return answer;
}