#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 1;
    for (int factorial = 1; factorial <= n; factorial *= answer) answer++;
    return answer - 1;
}