#include <string>
#include <vector>

using namespace std;

int solution(string binomial) {
    vector<string> oper(3);
    int i = 0;
    for(char chr: binomial) {
        if (chr == ' ') {i++; continue;}
        oper[i] += chr;
    }

    switch(oper[1][0]) {
        case '+': return stoi(oper[0]) + stoi(oper[2]);
        case '-': return stoi(oper[0]) - stoi(oper[2]);
        case '*': return stoi(oper[0]) * stoi(oper[2]);
    }
}