#include <string>
#include <vector>

using namespace std;

string solution(vector<int> numLog) {
    string answer = "";
    for (int i = 0; i < numLog.size() - 1; i++)
        switch(numLog[i] - numLog[i+1]){
            case 1:
                answer += 's';
                break;
            case -1:
                answer += 'w';
                break;
            case 10:
                answer += 'a';
                break;
            case -10:
                answer += 'd';
        }

    return answer;
}