#include <string>
#include <sstream>
#include <vector>

using namespace std;

vector<string> solution(string my_string) {
    vector<string> answer;
    istringstream iss(my_string);
    string temp;
    while(iss >> temp) answer.push_back(temp);
    return answer;
}