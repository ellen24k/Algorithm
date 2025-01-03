#include <string>
#include <vector>

using namespace std;

int solution(int num, int k) {
    string num_str = to_string(num);
    for (int idx = 0; idx < num_str.length(); idx++)
        if (num_str[idx] == k + '0') return ++idx;
    
    return -1;
}