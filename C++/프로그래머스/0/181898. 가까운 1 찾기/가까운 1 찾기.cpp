#include <string>
#include <vector>

using namespace std;

int solution(vector<int> arr, int idx) {
    for (int i = idx; i < arr.size(); i++){ // 문제 예시를 봤을 때 idx보다 크면서(x), idx보다 크거나 같으면서(o)
        if (arr[i] == 1) return i;
    }
    return -1;
}