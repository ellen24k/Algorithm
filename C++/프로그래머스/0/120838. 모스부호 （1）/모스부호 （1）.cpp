#include <string>
#include <map>
#include <sstream>

using namespace std;

string solution(string letter) {
    string answer = "";
    map<string, string> morse = {
        {".-","a"},
        {"-...","b"},
        {"-.-.","c"},
        {"-..","d"},
        {".","e"},
        {"..-.","f"},
        {"--.","g"},
        {"....","h"},
        {"..","i"},
        {".---","j"},
        {"-.-","k"},
        {".-..","l"},
        {"--","m"},
        {"-.","n"},
        {"---","o"},
        {".--.","p"},
        {"--.-","q"},
        {".-.","r"},
        {"...","s"},
        {"-","t"},
        {"..-","u"},
        {"...-","v"},
        {".--","w"},
        {"-..-","x"},
        {"-.--","y"},
        {"--..","z"}
    };

    istringstream origin_str(letter);
    string buff;
    while (getline(origin_str, buff, ' ')) 
        answer += morse[buff];
    return answer;
}