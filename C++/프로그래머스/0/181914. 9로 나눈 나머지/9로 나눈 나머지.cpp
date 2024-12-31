#include <string>

using namespace std;

int solution(string number) {
    int sum_of_number = 0;
    for (char num : number)
        sum_of_number += num - '0';
    
    return sum_of_number%9;
}