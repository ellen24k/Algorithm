#include <string>
#include <vector>

using namespace std;

int solution(string myString, string pat) {
    string converted = "";
    for (char c: myString){
        if (c=='A' or c=='B') converted += (c =='A') ? 'B' : 'A';
        else converted += c;
    }
    return (converted.find(pat) == string::npos) ? 0 : 1;
}