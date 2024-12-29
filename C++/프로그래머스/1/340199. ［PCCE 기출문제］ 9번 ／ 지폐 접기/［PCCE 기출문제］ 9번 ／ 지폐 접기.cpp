#include <string>
#include <iostream>
#include <vector>

using namespace std;

int solution(vector<int> wallet, vector<int> bill) {
    int answer = 0;
    int shorter = (bill[0] < bill[1]) ? 0 : 1;
    int longer = (bill[0] < bill[1]) ? 1 : 0;
    int w_shorter = min(wallet[0], wallet[1]);
    int w_longer = max(wallet[0], wallet[1]);

    while (w_longer < bill[longer] || w_shorter < bill[shorter]) {
        bill[longer] /= 2;
        answer++;
        
        shorter = (bill[0] < bill[1]) ? 0 : 1;
        longer = (bill[0] < bill[1]) ? 1 : 0;
        // cout << bill[0] << " " << bill[1] << endl;
    }
    return answer;
}